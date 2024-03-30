#!/usr/bin/python3
import requests
import sys

def list_commits(repo_name, owner_name):
    """
    List the 10 most recent commits of the repository and user on GitHub.

    Args:
        repo_name (str): The name of the repository.
        owner_name (str): The owner of the repository.
    """
    url = f"https://api.github.com/repos/Worof/alx-higher_level_programming/commits"
    response = requests.get(url)
    
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    else:
        print("Failed to retrieve commits.")

if __name__ == '__main__':
    if len(sys.argv) == 3:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        list_commits(repo_name, owner_name)
    else:
        print("Usage: {} <repository name> <owner name>".format(sys.argv[0]))
