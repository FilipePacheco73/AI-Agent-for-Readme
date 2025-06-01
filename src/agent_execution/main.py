# Libraries and modules
from auth.authentication_setup import _set_env
from prompts.prompt_template import system_message, human_message
from graph.agent_graph import main_agent
from logs.log import log_creation

# User Input examples for the agent
#user_input = 'How many files exists in this repository https://github.com/FilipePacheco73/AI-Agent-for-Readme?'
user_input = 'Can you create a Readme file for this repo https://github.com/FilipePacheco73/AI-Agent-for-Readme?'

# Invoke the main agent with the user input
messages = main_agent('gpt-4o').invoke({"messages": [system_message(), human_message(user_input)]})

# Log the creation of the agent with the messages
log_creation(messages)