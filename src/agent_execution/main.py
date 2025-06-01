# Libraries and modules
from auth.authentication_setup import _set_env
from prompts.prompt_template import system_message, human_message
from graph.agent_graph import main_agent
from logs.log import log_creation


# Set up the OpenAI API key
_set_env('OPENAI_API_KEY')


# Example input for the agent
user_input = 'What is included in this repository https://github.com/FilipePacheco73/AI-Agent-for-Readme?' 
user_input = 'How many files exists in this repository https://github.com/FilipePacheco73/AI-Agent-for-Readme?'
#user_input = 'Can you create a Readme file for this repo https://github.com/FilipePacheco73/AI-Agent-for-Readme?'
#user_input = 'Oi'

# Invoke the main agent with the user input
messages = main_agent('gpt-3.5-turbo-0125').invoke({"messages": [system_message(), human_message(user_input)]})

log_creation(messages)