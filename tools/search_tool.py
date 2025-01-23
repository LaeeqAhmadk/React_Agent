import time
from googlesearch import search
from utils.custom_logger import get_logger
from utils.exception import CustomException

logger = get_logger(__name__)

def searchingTool(query: str) -> str:
    """
    This tool searches the internet for the query that is being passed.
    This tool can be used for gathering the latest information about the topic.
    This tool uses Google's Search, and returns the context based on the top results obtained.

    Args:
        query: prompt from the agent
    Returns:
        context(str): a complete combined context
    """
    try:
        logger.info(f"Searching for query: {query}")
        time.sleep(1)
        response = search(query, num_results=20, advanced=True)
        context = "".join(result.description for result in response)
        logger.debug(f"Search results: {context}")
        return context
    except Exception as e:
        logger.error(f"Error in searchingTool: {str(e)}")
        raise CustomException("An error occurred in searchingTool", e)
