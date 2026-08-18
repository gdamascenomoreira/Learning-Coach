from profile_manager import (
    profile_exists,
    create_profile,
    save_profile,
    load_profile
)

from prompt_builder import SYSTEM_PROMPT, build_prompt
from ai_client import get_response


def get_profile():
    if profile_exists():
        return load_profile()

    profile = create_profile()
    save_profile(profile)

    return profile


def main():
    print("Learning Coach Started")
    print()

    profile = get_profile()

    print()
    print(f"Welcome, {profile.get('name', 'there')}!")
    print(f"Current role: {profile.get('current_role', 'Not provided')}")
    print(f"Career goal: {profile.get('career_goal', 'Not provided')}")
    print()

    question = input("Ask Learning Coach: ")

    prompt = build_prompt(profile, question)

    print()
    print("Learning Coach is thinking...")
    print()

    answer = get_response(
        SYSTEM_PROMPT,
        prompt
    )

    print("======== LEARNING COACH RESPONSE ========")
    print(answer)

if __name__ == "__main__":
    main()