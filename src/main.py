from new_user import username as create_user
from settings import settings_start
from types import ClassMethodDescriptorType
from typing import ClassVar
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
    def __init__(self, user):
        self.user = user

    def books_data_load(self):
        with open(f"{profile.name}_books_data.json", "r") as file:
            return json.load(file)

    def book_data_dump(self, data_export):
        with open(f"{profile.name}_books_data.json", "w") as file:
            json.dump(data_export, file, indent=4)

    def number_books(self):
        books_log = self.books_data_load()
        return len(books_log)

    def show_books(self):
        books_log = self.books_data_load()

        print("\nThis is your books collection:")
        for book in books_log:
            print(f" * {book} by {books_log[book]['author']}")

        menu()

    def add_book(self):
        book_id = self.number_books()

        title = pyip.inputStr("\n * Title: ")
        author = pyip.inputStr(" * Author: ")
        pages = pyip.inputInt(" * Number of pages: ")
        editorial = pyip.inputStr(" * Editorial: ")
        publishing_date = pyip.inputDate(
            " * Publishing date: ",
            formats=("%d/%m/%y", "%d.%m.%y", "%d-%m-%y", "%d %m %y"),
        )
        isbn = pyip.inputInt(" * ISBN: ")
        book_format = pyip.inputStr(" * Format: ")
        language = pyip.inputStr(" * Language: ")
        status = pyip.inputStr(" * Reading status: ")

        print("\nBook added correctly!!")

        new_book = Book(
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

        book_export = new_book.__dict__

        with open(f"{profile.name}_books_data.json", "r") as file:
            data = json.load(file)
            data[new_book.title] = book_export

        self.book_data_dump(data)
        menu()

    def update_book(self):
        books_log = self.books_data_load()
        self.show_books()

        book_update = pyip.inputStr("\nWhich book would you like to edit: ")
        if book_update not in books_log:
            print("This book does not exist.")
            self.update_book()
        else:
            current_book_info = Book(
                books_log[book_update]["title"],
                books_log[book_update]["author"],
                books_log[book_update]["pages"],
                books_log[book_update]["editorial"],
                books_log[book_update]["publishing_date"],
                books_log[book_update]["isbn"],
                books_log[book_update]["book_format"],
                books_log[book_update]["language"],
                books_log[book_update]["status"],
                books_log[book_update]["book_id"],
            )

            books_log.pop(current_book_info.title)

            book_id = current_book_info.book_id
            title = pyip.inputStr(
                f" * Current title: {current_book_info.title}\n   Edited title: "
            )
            author = pyip.inputStr(
                f"\n * Current author: {current_book_info.author}\n   Edited Author: "
            )
            pages = pyip.inputInt(
                f"\n * Current number of pages: {current_book_info.pages}\n   Edited number of pages: "
            )
            editorial = pyip.inputStr(
                f"\n * Current editorial: {current_book_info.editorial}\n   Edited editorial: "
            )
            publishing_date = pyip.inputDate(
                f"\n * Current publishing date: {current_book_info.publishing_date}\n   Edited publishing date: ",
                formats=("%d/%m/%y", "%d.%m.%y", "%d-%m-%y", "%d %m %y"),
            )
            isbn = pyip.inputInt(
                f"\n * Current ISBN: {current_book_info.isbn}\n   Edited ISBN: "
            )
            book_format = pyip.inputStr(
                f"\n * Current format: {current_book_info.book_format}\n   Edited format: "
            )
            language = pyip.inputStr(
                f"\n * Current language: {current_book_info.language}\n   Edited language: "
            )
            status = pyip.inputStr(
                f"\n * Current status: {current_book_info.status}\n   Edited Status: "
            )

            print("Book updated correctly!!")

            update_book_information = Book(
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

        book_export = update_book_information.__dict__
        books_log[update_book_information.title] = book_export
        self.book_data_dump(books_log)
        menu()

    def delete_book(self):
        books_log = self.books_data_load()
        self.show_books()

        book_delete = pyip.inputStr("\nWhich book would you like to delete  : ")
        if book_delete not in books_log:
            print("This book does not exist.")
            self.delete_book()
        else:
            del books_log[book_delete]
            self.book_data_dump(books_log)

            print("\nBook deleted correctly!!")
            menu()


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

        user_library = Library(profile.name)

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
        settings_start()
    else:
        exit()
