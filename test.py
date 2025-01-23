import sys
from llama_index.llms.gemini import Gemini
from llama_index.core.tools.function_tool import FunctionTool
from llama_index.core.agent import ReActAgent
from tools.search_tool import SearchingTool
from utils.custom_logger import logger
from utils.exception import CustomException

try:
    # Create a FunctionTool for the search functionality
    search_tool = FunctionTool.from_defaults(fn=SearchingTool)
    logger.info("FunctionTool for search created successfully.")

    # Initialize the Gemini LLM
    llm = Gemini()  # Ensure this is properly configured in your environment
    logger.info("Gemini LLM initialized successfully.")

    # Initialize the ReActAgent
    agent = ReActAgent.from_tools(
        tools=[search_tool],
        llm=llm,
        verbose=True,
        allow_parallel_tool_calls=True
    )
    logger.info("Initialized ReActAgent successfully.")

except Exception as e:
    # Log the error with detailed traceback
    logger.error(CustomException(e, sys))

print(dir(agent))