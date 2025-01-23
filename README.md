# React LLM Agent

This project integrates a **ReAct AI Agent** with a custom tool for querying real-time information using a Gemini language model. The agent can be customized to perform various actions, and this specific implementation is designed to search for information through a function tool.

## Project Structure

The project is organized into the following directories and files:

react_agent_app/ 

├── app.py # Streamlit app to interact with the ReAct Agent 

├── requirements.txt # Python dependencies for the project 

├── main.py # Main script to execute the agent's queries 

├── agents/ # Directory containing agent logic 

│ ├── react_agent.py # Configuration and setup of the ReAct agent 

├── tools/ # Directory containing external tools 

│ ├── search_tool.py # A custom search tool function for querying information 

├── utils/ # Utility functions and logging 

│ ├── custom_logger.py # Logger configuration 

│ ├── exception.py # Custom exceptions used in the project 

├── config/ # Configuration files for setting up the environment 

│ ├── settings.py # Stores environment variables and API keys

react_agent_app/ ├── app.py # Streamlit app to interact with the ReAct Agent ├── requirements.txt # Python dependencies for the project ├── main.py # Main script to execute the agent's queries ├── agents/ # Directory containing agent logic │ ├── react_agent.py # Configuration and setup of the ReAct agent ├── tools/ # Directory containing external tools │ ├── search_tool.py # A custom search tool function for querying information ├── utils/ # Utility functions and logging │ ├── custom_logger.py # Logger configuration │ ├── exception.py # Custom exceptions used in the project ├── config/ # Configuration files for setting up the environment │ ├── settings.py # Stores environment variables and API keys



## Features

- **ReAct AI Agent**: A robust AI agent powered by the Gemini language model that can perform parallel tool calls to gather data.
- **Custom Search Tool**: The agent is paired with a custom function tool to search for specific information, such as querying for general knowledge or domain-specific topics.
- **Logging and Error Handling**: The project is equipped with detailed logging to track agent behavior and catch exceptions.


## Usage
   - Interacting with the Agent: The ReAct agent will take user input (a query) and search for relevant information based on the tools available.
   - Customizing the Agent: You can easily modify the search_tool.py file or add new tools to expand the agent's capabilities.

     
## Contributing

If you'd like to contribute to the project, feel free to fork it and submit a pull request with your improvements.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](./LICENSE) file for more details.




