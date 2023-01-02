"""
Name: Mingyu Zhao
Date started: 29th December, 2022
Github URL:
"""
import csv
from csv import writer

MENU = "Menu:\nL - List all books\nA - Add new book\nM - Mark a book as completed\nQ - Quit"

print("Reading Tracker 1.0 - by MINGYU ZHAO")


def line_reader():
    with open("books.csv", "r") as in_file:
        reader = csv.reader(in_file)
        books = []
        for row in reader:
            books.append(row)
        return books


def list_books():
    with open("books.csv", "r") as data:
        line = csv.reader(data)
        for row, line in enumerate(line, start=1):
            state = complete_statue(line)
            print(f"{state}{row}.{line[0]} by {line[1]} {line[2]} pages")


def add_book():
    title = input("Title: ")
    author = input("Author: ")
    pages = int(input("Pages: "))
    states = "c"
    new_data = [title, author, pages, states]
    result = f"{title} by {author}, ({pages} pages) added to Reading Tracker"
    with open("books.csv", 'a') as new_book:
        add_new_book = writer(new_book)
        add_new_book.writerow(new_data)
    print(result)


def complete_statue(line):
    if line[3] == "r":
        return "*"
    else:
        return " "


def complete_book():
    list_books()
    count_book = 0
    if state == "*":
        count_book += 1
        line[2] += str(line[2])
    print(f"You need to read {line[2]} pages in {count_book} books.")
    finish_number = int(input("Enter the number of a book to mark as completed!\n>>>"))


def main():
    number_books = line_reader()
    print(f"{len(number_books)} books loaded")
    print(MENU)
    option = input(">>>").upper()
    while option != "Q":
        if option == "L":
            list_books()
        elif option == "A":
            add_book()
        elif option == "M":
            complete_book()
        else:
            print("Invalid menu choice")
        print(MENU)
        option = input(">>>").upper()
    print(f"{len(number_books)} save to books.csv")
    print("So many book, so little time. Frank Zappa")


line_reader()
main()
