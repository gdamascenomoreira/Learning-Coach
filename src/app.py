from profile_manager import load_profile
from prompt_builder import SYSTEM_PROMPT, build_prompt
from ai_client import get_response


def main():

    profile = load_profile()

    question = input("Ask Learning Coach: ")

    prompt = build_prompt(profile, question)

    print()
    print("Learning Coach is thinking...")
    print()

    answer = get_response(
        SYSTEM_PROMPT,
        prompt
    )

    print(answer)


if __name__ == "__main__":
    main()