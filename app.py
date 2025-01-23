import streamlit as st
from agents.react_agent import agent
from utils.custom_logger import get_logger
from utils.exception import CustomException

# Initialize logger
logger = get_logger(__name__)

def get_agent_response(query):
    try:
        logger.info(f"Executing query: {query}")
        # Use the agent to get a response for the provided query
        response = agent.chat(query)
        return response
    except CustomException as ce:
        logger.error(f"Custom exception occurred: {ce}")
        return f"Error: {ce}"
    except Exception as e:
        logger.error(f"Unhandled exception: {str(e)}")
        return f"Error: {str(e)}"

def main():
    st.title("ReAct LLM Agent")
    
    # Query input
    query = st.text_input("Enter your query:", "What is the name of the prime minister of Pakistan?")
    
    if query:
        # Get agent response for the input query
        response = get_agent_response(query)
        
        # Display the agent's response
        st.write("Agent's Response:")
        st.write(response)
    else:
        st.write("Please enter a query to begin.")

if __name__ == "__main__":
    main()
