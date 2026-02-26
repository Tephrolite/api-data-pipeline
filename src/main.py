from .api_client import get_user_repos
from .processor import transform_repo_data
from .database import insert_repositories, get_top_repositories


def run_pipeline(username: str):
    print(f"Fetching repositories for {username}...")

    raw_data = get_user_repos(username)
    transformed = transform_repo_data(raw_data)

    insert_repositories(transformed)

    print("Data inserted successfully.\n")

    print("Top repositories by stars:")
    top = get_top_repositories()

    for repo in top:
        print(f"{repo['name']} - ⭐ {repo['stars']}")


if __name__ == "__main__":
    run_pipeline("octocat")
