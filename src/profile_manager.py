import json

def load_profile():
    with open("user_profile.json", "r") as file:
        return json.load(file)