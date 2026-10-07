import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "users.json")


def load_users():
    """Load all users from the local JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read users.json. Starting with an empty user list.")
        return {}


def save_users(users):
    """Save all users permanently to the local JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)


def progress_bar(progress):
    """Create a simple 10-block progress bar."""
    filled = progress // 10
    empty = 10 - filled
    return "█" * filled + "░" * empty


def create_user(users):
    print("\n=== Create user ===")
    username = input("Choose a username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return None

    if username in users:
        print("That user already exists.")
        return None

    users[username] = {
        "skills": {}
    }
    save_users(users)
    print(f"User '{username}' created!")
    return username


def choose_user(users):
    """Let the person choose an existing user or create a new one."""
    while True:
        print("\n=== Skill Tree ===")

        usernames = list(users.keys())

        if usernames:
            print("Choose a user:")
            for number, username in enumerate(usernames, start=1):
                print(f"{number}. {username}")
        else:
            print("No users exist yet.")

        print(f"{len(usernames) + 1}. Create new user")
        print("0. Exit")

        choice = input("> ").strip()

        if choice == "0":
            return None

        if choice.isdigit():
            choice_number = int(choice)

            if 1 <= choice_number <= len(usernames):
                return usernames[choice_number - 1]

            if choice_number == len(usernames) + 1:
                new_user = create_user(users)
                if new_user is not None:
                    return new_user

        print("Invalid choice. Try again.")


def show_skills(user_data):
    skills = user_data["skills"]

    print("\n=== Your skills ===")

    if not skills:
        print("You have not added any skills yet.")
        return

    for number, (skill_name, progress) in enumerate(skills.items(), start=1):
        bar = progress_bar(progress)
        print(f"{number}. {skill_name:<20} [{bar}] {progress}%")


def add_skill(user_data):
    print("\n=== Add skill ===")
    skill_name = input("Skill name: ").strip()

    if not skill_name:
        print("Skill name cannot be empty.")
        return

    if skill_name in user_data["skills"]:
        print("That skill already exists.")
        return

    user_data["skills"][skill_name] = 0
    print(f"Added '{skill_name}' with 0% progress.")


def choose_skill(user_data):
    skills = list(user_data["skills"].keys())

    if not skills:
        print("You do not have any skills yet.")
        return None

    print("\nChoose a skill:")
    for number, skill in enumerate(skills, start=1):
        print(f"{number}. {skill}")

    choice = input("> ").strip()

    if choice.isdigit():
        choice_number = int(choice)
        if 1 <= choice_number <= len(skills):
            return skills[choice_number - 1]

    print("Invalid choice.")
    return None


def update_progress(user_data):
    skill = choose_skill(user_data)
    if skill is None:
        return

    print(f"Current progress in {skill}: {user_data['skills'][skill]}%")
    new_progress = input("New progress (0-100): ").strip()

    if not new_progress.isdigit():
        print("Progress must be a whole number from 0 to 100.")
        return

    new_progress = int(new_progress)

    if not 0 <= new_progress <= 100:
        print("Progress must be between 0 and 100.")
        return

    user_data["skills"][skill] = new_progress
    print(f"Updated {skill} to {new_progress}%.")


def remove_skill(user_data):
    skill = choose_skill(user_data)
    if skill is None:
        return

    confirm = input(f"Remove '{skill}'? (y/n): ").strip().lower()
    if confirm == "y":
        del user_data["skills"][skill]
        print(f"Removed '{skill}'.")
    else:
        print("Cancelled.")


def user_menu(users, username):
    while True:
        user_data = users[username]

        print(f"\n=== Welcome, {username}! ===")
        print("1. View skills")
        print("2. Add skill")
        print("3. Update progress")
        print("4. Remove skill")
        print("5. Switch user")
        print("0. Save and exit")

        choice = input("> ").strip()

        if choice == "1":
            show_skills(user_data)

        elif choice == "2":
            add_skill(user_data)
            save_users(users)

        elif choice == "3":
            update_progress(user_data)
            save_users(users)

        elif choice == "4":
            remove_skill(user_data)
            save_users(users)

        elif choice == "5":
            save_users(users)
            return "switch"

        elif choice == "0":
            save_users(users)
            return "exit"

        else:
            print("Invalid choice. Try again.")


def main():
    users = load_users()

    while True:
        username = choose_user(users)

        if username is None:
            save_users(users)
            print("Goodbye!")
            break

        result = user_menu(users, username)

        if result == "exit":
            print("Your progress has been saved. Goodbye!")
            break


if __name__ == "__main__":
    main()
