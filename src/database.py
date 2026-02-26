from pymongo import MongoClient
from .config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["api_data_pipeline"]
collection = db["github_repos"]


def insert_repositories(repos: list):
    if repos:
        collection.insert_many(repos)


def get_top_repositories(limit=5):
    return list(
        collection.find().sort("stars", -1).limit(limit)
    )
