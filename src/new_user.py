from os.path import exists
import json

titles = {
    "welcome": """
     -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    |                                   _______    _________      __      ________   ___  ____  _________ _______    _____    ____  ____                                    |
    |                                  |_   __ \  |_   ___  |    /  \    |_   ___ \.|_  ||_  _||_   ___  |_   __ \  |_   _|  |_  _||_  _|                                   |
    |                                    | |__) |   | |_  \_|   / /\ \     | |   \. \ | |_/ /    | |_  \_| | |__) |   | |      \ \  / /                                     |
    |                                    |  __ /    |  _|  _   / ____ \    | |    | | |  __'.    |  _|  _  |  __ /    | |   _   \ \/ /                                      |
    |                                   _| |  \ \_ _| |___/ |_/ /    \ \_ _| |___.' /_| |  \ \_ _| |___/ |_| |  \ \_ _| |__/ |  _|  |_                                      |
    |                                  |____| |___|_________|____|  |____|________.'|____||____|_________|____| |___|________| |______|                                     |
     -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    """,
    "books": """
     -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    |                                                            ______     ____     ____   ___  ____   _______                                                             |
    |                                                           |_   _ \  .'    \. .'    \.|_  ||_  _| /  ___  |                                                            |
    |                                                             | |_) |/  .--.  \  .--.  \ | |_/ /  |  (__ \_|                                                            |
    |                                                             |  __/.| |    | | |    | | |  __'.   '.___\-.                                                             |
    |                                                            _| |__) |  \--'  /  \--'  /_| |  \ \_|\_____) |                                                            |
    |                                                           |_______/ \.____.' \.____.'|____||____|_______.'                                                            |
     -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    """,
    "reading time": """
     -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    |                          _______    _________      __      ________   _____ ____  _____   ______       _________ _____ ____    ____ _________                          |
    |                         |_   __ \  |_   ___  |    /  \    |_   ___ \.|_   _|_   \|_   _|.' ___  |     |  _   _  |_   _|_   \  /   _|_   ___  |                         |
    |                           | |__) |   | |_  \_|   / /\ \     | |   \. \ | |   |   \ | | / .'   \_|     |_/ | | \_| | |   |   \/   |   | |_  \_|                         |
    |                           |  __ /    |  _|  _   / ____ \    | |    | | | |   | |\ \| | | |    ____        | |     | |   | |\  /| |   |  _|  _                          |
    |                          _| |  \ \_ _| |___/ |_/ /    \ \_ _| |___.' /_| |_ _| |_\   |_\ \.___]  _|      _| |_   _| |_ _| |_\/_| |_ _| |___/ |                         |
    |                         |____| |___|_________|____|  |____|________.'|_____|_____|\____|\._____.'       |_____| |_____|_____||_____|_________|                         |
     -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """,
    "reading schedule": """
     -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    |    _______    _________      __      ________   _____ ____  _____   ______        _______   ______ ____  ____ _________ ________   _____  _____ _____    _________    |
    |   |_   __ \  |_   ___  |    /  \    |_   ___ \.|_   _|_   \|_   _|.' ___  |      /  ___  |./ ___  |_   ||   _|_   ___  |_   ___ \.|_   _||_   _|_   _|  |_   ___  |   |
    |     | |__) |   | |_  \_|   / /\ \     | |   \. \ | |   |   \ | | / .'   \_|     |  (__ \_| ./   \_| | |__| |   | |_  \_| | |   \. \ | |    | |   | |      | |_  \_|   |
    |     |  __ /    |  _|  _   / ____ \    | |    | | | |   | |\ \| | | |    ____     '.___\-.| |        |  __  |   |  _|  _  | |    | | | '    ' |   | |   _  |  _|  _    |
    |    _| |  \ \_ _| |___/ |_/ /    \ \_ _| |___.' /_| |_ _| |_\   |_\ \.___]  _|   |\_____) | \.___.'\_| |  | |_ _| |___/ |_| |___.' /  \ \--' /   _| |__/ |_| |___/ |   |
    |   |____| |___|_________|____|  |____|________.'|_____|_____|\____|\._____.'     |_______.'\._____.'____||____|_________|________.'    \.__.'   |________|_________|   |
     -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """,
}

phrases = {
    "welcome": "Welcome to Readkerly!! I'm Kerly, your new personasl assistant.",
    "start": ", let's start by setting up your reading goals.",
    "username": "How should I  call you?: ",
    "books": "How many books do you want to read in a year?: ",
    "reading time": "How much time do you want to read per day? (mins): ",
    "reading schedule": "How many days do you want to read per week? (days): ",
    "press enter": "Press Enter to continue...",
}

user_information = {}


def enter_pressed(value, next_function, current_function):
    if value == "":
        next_function()
    else:
        print("Please enter a valid value.")
        current_function()


def reading_schedule_goal():
    global schedule_goal

    print(titles["reading schedule"])
    schedule_goal = input(phrases["reading schedule"])
    user_information["schedule_goal"] = schedule_goal

    with open("users_data.json", "r") as file:
        data = json.load(file)
        data[user_information["username"]] = user_information

    with open("users_data.json", "w") as file:
        json.dump(data, file, indent=4)

    with open(f"{user_information['username']}_books_data.json", "a") as file:
        json.dump({}, file)


def reading_time_goal():
    global time_goal

    print(titles["reading time"])
    time_goal = input(phrases["reading time"])
    user_information["time_goal"] = time_goal
    continue_value = input(phrases["press enter"])
    enter_pressed(continue_value, reading_schedule_goal, reading_time_goal)


def books_goal():
    global year_goal

    print(titles["books"])
    year_goal = input(phrases["books"])
    user_information["year_goal"] = year_goal
    continue_value = input(phrases["press enter"])
    enter_pressed(continue_value, reading_time_goal, books_goal)


def username():
    global username

    if not exists("users_data.json"):
        with open("users_data.json", "w") as file:
            json.dump({}, file)

    print(f"{titles['welcome']}\n{phrases['welcome']}")
    username = input(phrases["username"])
    user_information["username"] = username

    print(f"\n{username} {phrases['start']}")
    continue_value = input(phrases["press enter"])

    enter_pressed(continue_value, books_goal, username)
