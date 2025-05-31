# Libraries and modules
from auth.authentication_setup import _set_env
from prompts.prompt_template import system_message, human_message
from graph.agent_graph import main_agent

# Set up the OpenAI API key
_set_env('OPENAI_API_KEY')

# Example input for the agent
user_input = 'What are the contents of this repository https://github.com/FilipePacheco73/AI-Agent-for-Readme? How many files exists there?'
user_input = 'Can you create a Readme file for this repo https://github.com/FilipePacheco73/AI-Agent-for-Readme?'

messages = main_agent().invoke({"messages": [system_message(), human_message(user_input)]})

for m in messages["messages"]:
    m.pretty_print()