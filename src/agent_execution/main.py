from src.auth.authentication_setup import _set_env
from src.prompts.prompt_template import system_message, human_message
from src.graph.agent_graph import main_agent
from src.logs.log import log_creation

# Set up environment variables
_set_env("OPENAI_API_KEY")
_set_env("HF_TOKEN")
_set_env("TAVILY_API_KEY")
_set_env("GITHUB_TOKEN")

# User Input examples for the agent
#user_input = 'How many files exists in this repository https://github.com/FilipePacheco73/AI-Agent-for-Readme?'
user_input = 'Can you create a Readme file for this repo https://github.com/FilipePacheco73/AI-Agent-for-Readme?'

def run():
	print(f"User input: {user_input}")
	messages = main_agent('gpt-4o').invoke({"messages": [system_message(), human_message(user_input)]})
	log_creation(messages)

if __name__ == "__main__":
	run()