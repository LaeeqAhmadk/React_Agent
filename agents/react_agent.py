from llama_index.llms.gemini import Gemini
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import ReActAgent
from tools.search_tool import searchingTool
from utils.custom_logger import get_logger

logger = get_logger(__name__)

try:
    # Initialize the Gemini LLM
    logger.info("Initializing Gemini LLM...")
    llm = Gemini()

    # Create a FunctionTool for the search functionality
    logger.info("Setting up FunctionTool...")
    search_tool = FunctionTool.from_defaults(fn=searchingTool)

    # Initialize the ReActAgent with the search tool
    logger.info("Initializing ReActAgent...")
    agent = ReActAgent.from_tools(
        [search_tool],
        llm=llm,
        verbose=True,
        allow_parallel_tool_calls=True,
    )
except Exception as e:
    logger.error(f"Error setting up ReActAgent: {str(e)}")
    raise
