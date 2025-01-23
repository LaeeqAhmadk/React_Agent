from agents.react_agent import agent
from utils.custom_logger import get_logger
from utils.exception import CustomException

logger = get_logger(__name__)

def main():
    try:
        template = "What is the name of prime minister of Pakistan?"
        logger.info(f"Executing query: {template}")
        response = agent.chat(template)
        print(response)
    except CustomException as ce:
        logger.error(f"Custom exception occurred: {ce}")
    except Exception as e:
        logger.error(f"Unhandled exception: {str(e)}")

if __name__ == "__main__":
    main()
