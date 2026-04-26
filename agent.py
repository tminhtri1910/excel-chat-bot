import os
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import MessagesPlaceholder
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
        df = pd.read_excel(file_path)
        # Drop columns where ALL values are NaN
        df = df.dropna(axis=1, how='all')
    except Exception as e:
        return f"Error reading Excel file: {str(e)}"
    
    try:
        print(f"[Agent] Initializing LLM for query: {query}")
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            openai_api_key=os.environ.get("OPENAI_API_KEY"),
        )
        
        # Format history into a string to provide context manually
        # This works around version-specific prompt limitations
        history_text = ""
        if history:
            for msg in history:
                role = "User" if isinstance(msg, HumanMessage) else "AI"
                history_text += f"{role}: {msg.content}\n"
        
        # Combine history with the current query
        full_query = f"Below is the history of our conversation so far:\n{history_text}\nQuestion: {query}" if history_text else query

        # Create the pandas dataframe agent 
        # Note: allow_dangerous_code and extra_prompt_messages are handled manually here
        agent = create_pandas_dataframe_agent(
            llm,
            df,
            verbose=True,
            agent_type="openai-tools",
            agent_executor_kwargs={"handle_parsing_errors": True}
        )
        
        print("Executing query with manual context...")
        response = agent.invoke({"input": full_query})
        
        answer = response.get("output", "No response generated.")
        print(f"[Agent] Successfully generated answer.")
        return answer
    except Exception as e:
        error_msg = f"Error executing agent query: {str(e)}"
        print(f"[Agent] {error_msg}")
        return error_msg
