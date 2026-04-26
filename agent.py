import os
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from dotenv import load_dotenv

# Load environment variables (e.g., OPENROUTER_API_KEY)
load_dotenv()

def query_excel(file_path: str, query: str, history: list = None) -> str:
    """
    Reads an Excel file into a pandas DataFrame and uses a Langchain 
    pandas agent to answer queries while remembering chat history.
    """
    try:
        # Load the Excel file into a pandas DataFrame
        df = pd.read_excel(file_path, usecols='A:H', skiprows=8)
    except Exception as e:
        return f"Error reading Excel file: {str(e)}"
    
    try:
        print(f"[Agent] Initializing LLM for query: {query}")
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            openai_api_key=os.environ.get("OPENAI_API_KEY"),
        )
        
        # Create the pandas dataframe agent with memory support
        agent = create_pandas_dataframe_agent(
            llm,
            df,
            verbose=True,
            agent_type="openai-tools",
            allow_dangerous_code=True, # MANDATORY
        )
        agent.handle_parsing_errors=True

        # Format the input to include history
        input_data = {
            "input": query,
            "chat_history": history if history is not None else []
        }

        print("input data:", input_data)
        
        print(f"[Agent] Executing query...")
        response = agent.invoke(input_data)
        
        answer = response.get("output", "No response generated.")
        print(f"[Agent] Successfully generated answer.")
        return answer
    except Exception as e:
        error_msg = f"Error executing agent query: {str(e)}"
        print(f"[Agent] {error_msg}")
        return error_msg
