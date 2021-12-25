from new_user import username as create_user
from types import ClassMethodDescriptorType
from typing import ClassVar
from os.path import exists
import pyinputplus as pyip
import json


class User:
    def __init__(self, name, year_goal, time_goal, schedule_goal):
        self.name = name
        self.year_goal = year_goal
        self.time_goal = time_goal
        self.schedule_goal = schedule_goal


class Book:
    def __init__(
        self,
        title,
        author,
        pages,
        editorial,
        publishing_date,
        isbn,
        book_format,
        language,
        status,
        book_id,
    ):
        self.title = title
        self.author = author
        self.pages = pages
        self.editorial = editorial
        self.publishing_date = publishing_date
        self.isbn = isbn
        self.book_format = book_format
        self.language = language
        self.status = status
        self.book_id = book_id


class Library:
    def __init__(self, user, number_books):
        self.user = user
        self.number_books = number_books

    def show_books(self):
        for book in self.number_books:
            print(f"{book.title} by {book.author}")

    def add_book(self):
        book_id = self.number_books
        self.number_books += 1

        title = pyip.inputStr("Title: ")
        author = pyip.inputStr("Author: ")
        pages = pyip.inputInt("Pages: ")
        editorial = pyip.inputStr("Editorial: ")
        publishing_date = pyip.inputDate(
            "Publishing date: ",
            formats=("%d/%m/%y", "%d.%m.%y", "%d-%m-%y", "%d %m %y"),
        )
        isbn = pyip.inputInt("ISBN: ")
        book_format = pyip.inputStr("Format: ")
        language = pyip.inputStr("Language: ")
        status = pyip.inputStr("Status: ")

        print("Book added correctly!!")

        book = Book(
            title,
            author,
            pages,
            editorial,
            str(publishing_date),
            isbn,
            book_format,
            language,
            status,
            book_id,
        )

        book_export = book.__dict__

        with open(f"{profile.name}_books_data.json", "r") as file:
            data = json.load(file)
            data[book.title] = book_export

        with open(f"{profile.name}_books_data.json", "w") as file:
            json.dump(data, file, indent=4)

    def update_book(self, book):
        book_update = pyip.inputStr("Which book would you like to edit: ")


def user_info(user):
    global profile
    global user_library

    with open("users_data.json", "r") as file:
        user_information = json.load(file)
        profile = User(
            user_information[f"{user}"]["username"],
            user_information[f"{user}"]["year_goal"],
            user_information[f"{user}"]["time_goal"],
            user_information[f"{user}"]["schedule_goal"],
        )

        user_library = Library(profile.name, 0)

    menu()


def menu():
    menu_action = pyip.inputInt(
        """
    1. Add book
    2. Update book
    3. Delete book
    4. Show books
    5. Settings
    6. Exit
    """,
        min=1,
        max=6,
    )

    menu_action_check(menu_action)


def menu_action_check(menu_action):
    if menu_action == 1:
        user_library.add_book()
    elif menu_action == 2:
        user_library.update_book()
    elif menu_action == 3:
        user_library.delete_book()
    elif menu_action == 4:
        user_library.show_books()
    elif menu_action == 5:
        user_library.settings()
    else:
        exit()
