#!/usr/bin/python3
import requests
import sys

def fetch_github_id(username, token):
    """
    Fetches the GitHub ID for the given username using GitHub API and token for authentication.

    Args:
        username (str): The GitHub username.
        token (str): The GitHub Personal Access Token.

    Returns:
        str: The GitHub user ID if the credentials are correct; 'None' otherwise.
    """
    url = f'https://api.github.com/users/Worof'
    response = requests.get(url, auth=(username, token))
    
    if response.status_code == 200:
        return response.json().get('id')
    else:
        return None

if __name__ == '__main__':
    if len(sys.argv) == 3:
        username = sys.argv[1]
        token = sys.argv[2]
        print(fetch_github_id(username, token))
    else:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
