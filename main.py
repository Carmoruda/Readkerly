from typing import ClassVar
import login


class User:
    def __init__(self, username, year_goal, time_goal, schedule_goal):
        self.username = username
        self.year_goal = year_goal
        self.time_goal = time_goal
        self.schedule_goal = schedule_goal


login
