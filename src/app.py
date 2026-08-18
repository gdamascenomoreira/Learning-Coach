from profile_manager import (
    profile_exists,
    create_profile,
    save_profile,
    load_profile
)

if not profile_exists():

    profile = create_profile()

    save_profile(profile)

else:

    profile = load_profile()

print()
print("Loaded Profile:")
print(profile)