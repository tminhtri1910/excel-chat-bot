import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import shutil

from agent import query_excel

app = FastAPI(title="Excel Chat Bot")

# Ensure an upload directory exists
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Mount static files for the frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/api/history")
async def get_history(file_path: str):
    """
    Returns the chat history for a specific file.
    """
    norm_path = os.path.normpath(file_path)
    if norm_path not in chat_histories:
        return {"history": []}
    
    # Convert LangChain messages to simple JSON-friendly format
    history = []
    for msg in chat_histories[norm_path]:
        history.append({
            "role": "user" if isinstance(msg, HumanMessage) else "assistant",
            "content": msg.content
        })
    return {"history": history}

@app.get("/api/files")
async def list_files():
    """
    Returns a list of all uploaded files in the uploads directory.
    """
    if not os.path.exists(UPLOAD_DIR):
        return {"files": []}
    
    files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(('.xlsx', '.xls', '.csv'))]
    if not files:
        return {"files": []}
    
    # Sort by modification time to get latest first
    files.sort(key=lambda x: os.path.getmtime(os.path.join(UPLOAD_DIR, x)), reverse=True)
    
    file_list = []
    for f in files:
        file_list.append({
            "filename": f,
            "file_path": os.path.join(UPLOAD_DIR, f)
        })
    
    return {"files": file_list}

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html", "r") as f:
        return f.read()

@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Endpoint to upload an Excel file.
    Returns the file path to be used in subsequent queries.
    """
    if not file.filename.endswith(('.xlsx', '.xls', '.csv')):
        raise HTTPException(status_code=400, detail="Invalid file type. Only Excel or CSV files are allowed.")
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return {"filename": file.filename, "file_path": file_path, "message": "File uploaded successfully."}

from langchain_core.messages import HumanMessage, AIMessage

# In-memory storage for chat history
# Format: { "normalized_path": [HumanMessage(...), AIMessage(...), ...] }
chat_histories = {}

@app.post("/api/chat")
async def chat(file_path: str = Form(...), query: str = Form(...)):
    """
    Endpoint to ask a question about the uploaded Excel file with context.
    """
    # Normalize path to ensure it works as a consistent dictionary key
    norm_path = os.path.normpath(file_path)
    
    print(f"[Server] Received query: '{query}' for file: {norm_path}")
    if not os.path.exists(norm_path):
        print(f"[Server] File not found: {norm_path}")
        raise HTTPException(status_code=404, detail="File not found. Please upload it again.")
    
    # Get existing history or initialize new one
    if norm_path not in chat_histories:
        chat_histories[norm_path] = []
    
    history = chat_histories[norm_path]
    print(f"[Server] Current history size: {len(history)} messages")
    
    # Run the query through our agent with history
    answer = query_excel(norm_path, query, history=history)
    
    # Update history (User message then AI message)
    history.append(HumanMessage(content=query))
    history.append(AIMessage(content=answer))
    
    # Keep history manageable (e.g., last 10 messages)
    if len(history) > 10:
        chat_histories[norm_path] = history[-10:]
    
    return {"answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
