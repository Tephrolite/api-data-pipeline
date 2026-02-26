import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

if not GITHUB_TOKEN:
    raise ValueError("Missing GITHUB_TOKEN in environment")

if not MONGO_URI:
    raise ValueError("Missing MONGO_URI in environment")
