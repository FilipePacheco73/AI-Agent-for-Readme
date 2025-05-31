import json
from langchain_openai import ChatOpenAI
from auth.authentication_setup import _set_env
from tools.tool_util import list_repo_contents, read_content

# Test OpenAI API key setup
def test_openai_api_key():
    try:
        _set_env('OPENAI_API_KEY')
        llm = ChatOpenAI(model_name='gpt-3.5-turbo-0125')
        response = llm.invoke('Hello, world!')
        print(f"OpenAI API key is set and working: {response.content}")
    except Exception as e:
        print(f"An error occurred with OpenAI API key: {e}")
        raise

# Test the get_tool_list function
def test_list_repo_contents():
    try:
        contents = list_repo_contents('FilipePacheco73', 'AI-Agent-for-Readme')
        print(f"Contents in the repo: \n{json.dumps(contents, indent=2)}")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

# Test the read_content function
def test_read_content():
    try:
        content = read_content('FilipePacheco73', 'AI-Agent-for-Readme', 'README.md')
        print(f"Content of README.md:\n{json.dumps(content, indent=2)}")
    except Exception as e:
        print(f"An error occurred while reading content: {e}")
        raise

if __name__ == "__main__":
    print("\n")
    test_openai_api_key()
    print("\n")
    test_list_repo_contents()
    print("\n")
    test_read_content()