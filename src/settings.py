import pyinputplus as pyip
from login import start
import main
import json


def user_info(user):
    global profile
    global user_library

    with open("users_data.json", "r") as file:
        user_information = json.load(file)
        profile = main.User(
            user_information[f"{user}"]["username"],
            user_information[f"{user}"]["year_goal"],
            user_information[f"{user}"]["time_goal"],
            user_information[f"{user}"]["schedule_goal"],
        )


def settings_start():
    settings_action = pyip.inputInt(
        """
    1. Account Settings
    2. Import & Export
    3. Terms and privacy policy
    4. Support us
    5. Contact us
    6. Sign out
    """,
        min=1,
        max=6,
    )

    settings_action_check(settings_action)


def settings_action_check(settings_action):
    if settings_action == 1:
        user_library.add_book()
    elif settings_action == 2:
        user_library.update_book()
    elif settings_action == 3:
        user_library.delete_book()
    elif settings_action == 4:
        user_library.show_books()
    elif settings_action == 5:
        settings_start()
    else:
        start()


settings_start()
