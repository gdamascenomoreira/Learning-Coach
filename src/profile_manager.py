import json
from pathlib import Path

PROFILE_PATH = Path("data/user_profile.json")


def profile_exists():
    return PROFILE_PATH.exists()


def load_profile():
    with open(PROFILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def save_profile(profile):
    with open(PROFILE_PATH, "w", encoding="utf-8") as file:
        json.dump(profile, file, indent=4)

def create_profile():

    print("Welcome to Learning Coach!")
    print("Let's create your profile.")
    print()

    name = input("What is your name? ")

    role = input("What is your current role? ")

    goal = input("What is your career goal? ")

    hours = input("How many hours per week can you dedicate to learning? ")

    profile = {
        "name": name,
        "current_role": role,
        "experience": "",
        "career_goal": goal,
        "weekly_learning_hours": int(hours),
        "certifications": [],
        "skills": [],
        "projects": [],
        "books": [],
        "courses": [],
        "interests": [],
        "completed_learning_activities": [],
        "learning_goals": [],
        "career_milestones": []
    }

    return profile