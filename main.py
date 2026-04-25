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

@app.get("/api/files")
async def list_files():
    """
    Returns the most recently uploaded file in the uploads directory.
    """
    if not os.path.exists(UPLOAD_DIR):
        return {"file": None}
    
    files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(('.xlsx', '.xls', '.csv'))]
    if not files:
        return {"file": None}
    
    # Sort by modification time to get the latest
    files.sort(key=lambda x: os.path.getmtime(os.path.join(UPLOAD_DIR, x)), reverse=True)
    latest_file = files[0]
    
    return {
        "filename": latest_file,
        "file_path": os.path.join(UPLOAD_DIR, latest_file)
    }

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

@app.post("/api/chat")
async def chat(file_path: str = Form(...), query: str = Form(...)):
    """
    Endpoint to ask a question about the uploaded Excel file.
    """
    print(f"[Server] Received query: '{query}' for file: {file_path}")
    if not os.path.exists(file_path):
        print(f"[Server] File not found: {file_path}")
        raise HTTPException(status_code=404, detail="File not found. Please upload it again.")
    
    # Run the query through our agent
    answer = query_excel(file_path, query)
    
    return {"answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
