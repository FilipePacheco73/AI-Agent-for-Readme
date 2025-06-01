import json
from langchain_openai import ChatOpenAI
from auth.authentication_setup import _set_env
from tools.tool_util import fetch_repo_structure, get_repo_commits, get_contributors, get_repo_info, get_languages, get_tags, get_branches, get_issues, get_pull_requests, get_releases

# Set environment variables for OpenAI API key and GitHub token
_set_env('GITHUB_TOKEN')
_set_env('OPENAI_API_KEY')

# Test OpenAI API key setup
def test_openai_api_key():
    try:
        llm = ChatOpenAI(model_name='gpt-3.5-turbo-0125')
        response = llm.invoke('Hello, world!')
        print(f"OpenAI API key is set and working: {response.content}")
    except Exception as e:
        print(f"An error occurred with OpenAI API key: {e}")
        raise

# Test fetch_repo_structure function
def test_fetch_repo_structure():
    try:
        structure = fetch_repo_structure('FilipePacheco73', 'AI-Agent-for-Readme')
        print(f"Repository structure:\n{json.dumps(structure, indent=2)}")
    except Exception as e:
        print(f"An error occurred while fetching repository structure: {e}")
        raise

# Test the commit history function
def test_get_repo_commits():
    try:
        commits = get_repo_commits('FilipePacheco73', 'AI-Agent-for-Readme')
        print(f"Commit history:\n{json.dumps(commits, indent=2)}")
    except Exception as e:
        print(f"An error occurred while fetching commits: {e}")
        raise

# Test the contributors function
def test_get_contributors():
    try:
        contributors = get_contributors('FilipePacheco73', 'AI-Agent-for-Readme')
        print(f"Contributors:\n{json.dumps(contributors, indent=2)}")
    except Exception as e:
        print(f"An error occurred while fetching contributors: {e}")
        raise

# Test the get_repo_info function
def test_get_repo_info():
    try:
        repo_info = get_repo_info('FilipePacheco73', 'AI-Agent-for-Readme')
        print(f"Repository info:\n{json.dumps(repo_info, indent=2)}")
    except Exception as e:
        print(f"An error occurred while fetching repository info: {e}")
        raise

# Test the get_languages function
def test_get_languages():
    try:
        languages = get_languages('FilipePacheco73', 'AI-Agent-for-Readme')
        print(f"Languages used in the repository:\n{json.dumps(languages, indent=2)}")
    except Exception as e:
        print(f"An error occurred while fetching languages: {e}")
        raise

# Test the get_tags function
def test_get_tags():
    try:
        tags = get_tags('FilipePacheco73', 'AI-Agent-for-Readme')
        print(f"Tags in the repository:\n{json.dumps(tags, indent=2)}")
    except Exception as e:
        print(f"An error occurred while fetching tags: {e}")
        raise

# Test the get_branches function
def test_get_branches():
    try:
        branches = get_branches('FilipePacheco73', 'AI-Agent-for-Readme')
        print(f"Branches in the repository:\n{json.dumps(branches, indent=2)}")
    except Exception as e:
        print(f"An error occurred while fetching branches: {e}")
        raise

# Test the get_issues function
def test_get_issues():
    try:
        issues = get_issues('FilipePacheco73', 'AI-Agent-for-Readme')
        print(f"Issues in the repository:\n{json.dumps(issues, indent=2)}")
    except Exception as e:
        print(f"An error occurred while fetching issues: {e}")
        raise

# Test the get_pull_requests function
def test_get_pull_requests():
    try:
        pull_requests = get_pull_requests('FilipePacheco73', 'AI-Agent-for-Readme')
        print(f"Pull requests in the repository:\n{json.dumps(pull_requests, indent=2)}")
    except Exception as e:
        print(f"An error occurred while fetching pull requests: {e}")
        raise

# Test the get_releases function
def test_get_releases():
    try:
        releases = get_releases('FilipePacheco73', 'AI-Agent-for-Readme')
        print(f"Releases in the repository:\n{json.dumps(releases, indent=2)}")
    except Exception as e:
        print(f"An error occurred while fetching releases: {e}")
        raise


if __name__ == "__main__":
    print("\n")
    test_openai_api_key()
    print("\n")
    test_fetch_repo_structure()
    print("\n")
    test_get_repo_commits()
    print("\n")
    test_get_contributors()
    print("\n")
    test_get_repo_info()
    print("\n")
    test_get_languages()
    print("\n")
    test_get_tags()
    print("\n")
    test_get_branches()
    print("\n")
    test_get_issues()
    print("\n")
    test_get_pull_requests()
    print("\n")
    test_get_releases()
    print("\n")