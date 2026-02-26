import requests
from .config import GITHUB_TOKEN


def get_user_repos(username: str):
    url = f"https://api.github.com/users/{username}/repos"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(
            f"GitHub API error {response.status_code}: {response.text}"
        )

    return response.json()
