from new_user import username as create_user
from main import user_info as info_main
from settings import user_info as info_settings
from os.path import exists
import pyinputplus as pyip
import json


def start():
    while not exists("users_data.json"):
        create_user()

    print("\nWelcome back to Readkerly!! What would you like to do?")
    action = pyip.inputInt(
        """
    1. Login to an existing account.
    2. Create a new account.
    3. Exit.
    """,
        min=1,
        max=3,
    )
    action_check(action)


def action_check(action):
    if action == 1:
        with open("users_data.json", "r") as file:
            users_log = json.load(file)

        print("\nThis is the list of users:")
        for user in users_log:
            print(f" * {user}")

        username = pyip.inputStr("\nPlease select a user: ")
        if username not in users_log:
            print("This user does not exist.")
            action_check(1)
        else:
            info_main(username)
            info_settings(username)

    elif action == 2:
        print("\n")
        create_user()
    else:
        exit()


start()
