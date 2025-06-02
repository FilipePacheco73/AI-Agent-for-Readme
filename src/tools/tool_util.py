import os
import requests
from auth.authentication_setup import _set_env

# Set up the GitHub token for authentication
_set_env('GITHUB_TOKEN')

headers = {
    'Authorization': f'token {os.getenv("GITHUB_TOKEN")}',
}

def fetch_repo_structure(owner: str, repo: str, path: str = '') -> dict:
    """
    Recursively fetch the structure of a GitHub repository.
    For directories, lists their contents.
    For specific file types, reads the first 10000 characters of their content.

    :param owner: The owner of the repository.
    :param repo: The name of the repository.
    :param path: The path within the repository.
    :return: A nested dictionary with repository structure and file previews.
    """
    repo_content = dict()

    # Set of file extensions and filenames to read
    readable_extensions = {'.txt', '.md', '.py', '.js', '.java', '.cpp', '.c', '.go', '.rs', '.sh', 
                           '.json', '.yaml', '.yml', '.toml', '.ini', '.cfg'}
    readable_filenames = {'LICENSE', 'README', 'README.md'}

    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        for item in response.json():
            item_data = {
                'type': item['type'],
                'path': item['path'],
                'html_url': item.get('html_url', None),
            }

            if item['type'] == 'dir':
                # Recursively searches the contents of the directory
                item_data['contents'] = fetch_repo_structure(owner, repo, item['path'])

            elif item['type'] == 'file':
                filename = item['name']
                _, ext = os.path.splitext(filename)

                # Check whether to read the content
                if ext.lower() in readable_extensions or filename in readable_filenames:
                    raw_url = f'https://raw.githubusercontent.com/{owner}/{repo}/main/{item["path"]}'
                    file_response = requests.get(raw_url, headers=headers)
                    if file_response.status_code == 200:
                        item_data['content_preview'] = file_response.text[:10000]  # 10k chars limit
                    else:
                        item_data['content_preview'] = f"Failed to fetch content: {file_response.status_code}"

            repo_content[item['name']] = item_data

        return repo_content
    else:
        response.raise_for_status()


def get_repo_commits(owner: str, repo: str) -> dict:
    """
    Get the commit history of a GitHub repository.

    :param owner: The owner of the repository.
    :param repo: The name of the repository.
    :return: A list of commit messages and their authors.
    """
    commits = dict()

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        for commit in response.json():
            commits[commit['sha']] = {
                'message': commit['commit']['message'],
                'author': commit['commit']['author']['name'],
                'date': commit['commit']['author']['date']
            }
        return commits
    else:
        response.raise_for_status()

def get_contributors(owner: str, repo: str) -> dict:
    """
    Get the contributors of a GitHub repository.

    :param owner: The owner of the repository.
    :param repo: The name of the repository.
    :return: A list of contributors with their contributions.
    """
    contributors = dict()

    url = f'https://api.github.com/repos/{owner}/{repo}/contributors'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        for contributor in response.json():
            contributors[contributor['login']] = {
                'contributions': contributor['contributions'],
                'html_url': contributor['html_url']
            }
        return contributors
    else:
        response.raise_for_status()

def get_repo_info(owner: str, repo: str) -> dict:
    """
    Get basic information about a GitHub repository.

    :param owner: The owner of the repository.
    :param repo: The name of the repository.
    :return: A dictionary containing repository information.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_languages(owner: str, repo: str) -> dict:
    """
    Get the programming languages used in a GitHub repository.

    :param owner: The owner of the repository.
    :param repo: The name of the repository.
    :return: A dictionary with languages and their respective bytes of code.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/languages'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_tags(owner: str, repo: str) -> dict:
    """
    Get the tags of a GitHub repository.

    :param owner: The owner of the repository.
    :param repo: The name of the repository.
    :return: A list of tags in the repository.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/tags'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_branches(owner: str, repo: str) -> dict:
    """
    Get the branches of a GitHub repository.

    :param owner: The owner of the repository.
    :param repo: The name of the repository.
    :return: A list of branches in the repository.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/branches'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_issues(owner: str, repo: str) -> dict:
    """
    Get the issues of a GitHub repository.

    :param owner: The owner of the repository.
    :param repo: The name of the repository.
    :return: A list of issues in the repository.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/issues'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_pull_requests(owner: str, repo: str) -> dict:
    """
    Get the pull requests of a GitHub repository.

    :param owner: The owner of the repository.
    :param repo: The name of the repository.
    :return: A list of pull requests in the repository.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_releases(owner: str, repo: str) -> dict:
    """
    Get the releases of a GitHub repository.

    :param owner: The owner of the repository.
    :param repo: The name of the repository.
    :return: A list of releases in the repository.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/releases'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()