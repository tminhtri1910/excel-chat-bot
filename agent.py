import os
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from dotenv import load_dotenv

# Load environment variables (e.g., OPENROUTER_API_KEY)
load_dotenv()

def query_excel(file_path: str, query: str) -> str:
    """
    Reads an Excel file into a pandas DataFrame and uses a Langchain 
    pandas agent (powered by OpenRouter) to execute Python code and answer the query.
    """
    try:
        # Load the Excel file into a pandas DataFrame
        df = pd.read_excel(file_path)
    except Exception as e:
        return f"Error reading Excel file: {str(e)}"
    
    try:
        # Initialize the OpenRouter LLM
        # Make sure OPENROUTER_API_KEY is in the environment
        print(f"[Agent] Initializing LLM with OpenRouter for query: {query}")
        llm = ChatOpenAI(
            model="nvidia/nemotron-3-super-120b-a12b:free", # OpenRouter requires vendor/model syntax like anthropic/claude-3.5-sonnet, openai/gpt-4o, google/gemini-pro
            temperature=0,
            openai_api_key=os.environ.get("OPENROUTER_API_KEY"),
            openai_api_base="https://openrouter.ai/api/v1",
        )
        
        # Create the pandas dataframe agent
        agent = create_pandas_dataframe_agent(
            llm,
            df,
            verbose=True,
            handle_parsing_errors=True,
            agent_type="zero-shot-react-description",
        )
        
        # Run the query
        print(f"[Agent] Executing query on dataframe...")
        response = agent.invoke({"input": query})
        
        answer = response.get("output", "No response generated.")
        print(f"[Agent] Successfully generated answer.")
        return answer
    except Exception as e:
        error_msg = f"Error executing agent query: {str(e)}"
        print(f"[Agent] {error_msg}")
        return error_msg
