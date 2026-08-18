import json
from pathlib import Path

PROFILE_PATH = Path("data/user_profile.json")


def profile_exists():
    return PROFILE_PATH.exists()


def load_profile():
    with open(PROFILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)
