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

    experience = input(
        "Briefly describe your experience: "
    )
    goal = input("What is your career goal? ")
    
    certifications = input("List your certifications separated by commas: ")
    certifications_list = [
    cert.strip()
    for cert in certifications.split(",")
    if cert.strip()
    ]

    skills = input("List your skills separated by commas: ")
    skills_list = [
    skill.strip()
    for skill in skills.split(",")
    if skill.strip()
    ]

    interests = input(
    "What are you interested in learning? "
    )
    interests_list = [
        interest.strip()
        for interest in interests.split(",")
        if interest.strip()
    ]
    
    while True:
        try:
            hours = int(
                input(
                    "How many hours per week can you dedicate to learning? "
                )
            )
            break
        except ValueError:
            print("Please enter a number.")
    
    profile = {
    "name": name,
    "current_role": role,
    "experience": experience,
    "career_goal": goal,
    "weekly_learning_hours": hours,
    "certifications": certifications_list,
    "skills": skills_list,
    "interests": interests_list,

    "projects": [],
    "books": [],
    "courses": [],
    "completed_learning_activities": [],
    "learning_goals": [],
    "career_milestones": []
}

    return profile

def show_profile_summary(profile):

    print()
    print("=" * 50)
    print("PROFILE SUMMARY")
    print("=" * 50)

    print(f"Name: {profile['name']}")
    print(f"Role: {profile['current_role']}")
    print(f"Experience: {profile['experience']}")
    print(f"Career Goal: {profile['career_goal']}")
    print(f"Weekly Learning Hours: {profile['weekly_learning_hours']}")

    print()

    print("Certifications:")
    for cert in profile["certifications"]:
        print(f" - {cert}")

    print()

    print("Skills:")
    for skill in profile["skills"]:
        print(f" - {skill}")

    print()

    print("Interests:")
    for interest in profile["interests"]:
        print(f" - {interest}")

    print()

    print("Projects:")
    for project in profile["projects"]:
        print(f" - {project}")

    print()

    print("Books:")
    for book in profile["books"]:
        print(f" - {book}")

    print()

    print("Courses:")
    for course in profile["courses"]:
        print(f" - {course}")

    print()

    print("Completed Learning Activities:")
    for activity in profile["completed_learning_activities"]:
        print(f" - {activity}")

    print()

    print("Learning Goals:")
    for goal in profile["learning_goals"]:
        print(f" - {goal}")

    print()

    print("Career Milestones:")
    for milestone in profile["career_milestones"]:
        print(f" - {milestone}")

    print("=" * 50)
    print()