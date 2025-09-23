# Libraries and modules
import sys
import os

# Setup project path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from path_setup import setup_project_path

from auth.authentication_setup import _set_env
from prompts.prompt_template import system_message, human_message
from graph.agent_graph import main_agent
from logs.log import log_creation

# Set up environment variables
_set_env("OPENAI_API_KEY")
_set_env("HF_TOKEN")
_set_env("TAVILY_API_KEY")
_set_env("GITHUB_TOKEN")

# User Input examples for the agent
#user_input = 'How many files exists in this repository https://github.com/FilipePacheco73/AI-Agent-for-Readme?'
user_input = 'Can you create a Readme file for this repo https://github.com/FilipePacheco73/AI-Agent-for-Readme?'

# Invoke the main agent with the user input
messages = main_agent('gpt-4o').invoke({"messages": [system_message(), human_message(user_input)]})

# Log the creation of the agent with the messages
log_creation(messages)