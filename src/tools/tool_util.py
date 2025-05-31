import requests

def list_repo_contents(owner: str, repo: str, path: str = '') -> dict:
    """
    List the contents of a GitHub repository at a specific path.

    :param owner: The owner of the repository.
    :param repo: The name of the repository.
    :param path: The path within the repository to list contents from.
    :return: A list of dictionaries containing file information.
    """
    repo_content = dict()

    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    response = requests.get(url)
    
    if response.status_code == 200:
        for item in response.json():
            repo_content[item['name']] = {
                'type': item['type'],
                'path': item['path'],
                'html_url': item.get('html_url', None),
            }

            if item['type'] == 'dir':
                # Recursively get contents of the directory
                repo_content[item['name']]['contents'] = list_repo_contents(owner, repo, item['path'])

        return repo_content

    else:
        response.raise_for_status()

def read_content(owner: str, repo: str, path: str) -> dict:
    """
    Read the content of a file in a GitHub repository.

    :param owner: The owner of the repository.
    :param repo: The name of the repository.
    :param path: The path to the file within the repository.
    :return: The content of the file as a string.
    """
    file_content = dict()

    url = f'https://raw.githubusercontent.com/{owner}/{repo}/main/{path}'
    response = requests.get(url)
    
    if response.status_code == 200:
        file_content[f"{owner}_{repo}_{path}"] = response.text[:10000]  # Limit to first 10000 characters for preview
        return file_content
    else:
        response.raise_for_status()