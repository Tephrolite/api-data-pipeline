from datetime import datetime, timezone


def transform_repo_data(repos: list):
    cleaned = []

    for repo in repos:
        cleaned.append({
            "repo_id": repo["id"],
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "language": repo["language"],
            "collected_at": datetime.now(timezone.utc)
        })

    return cleaned
