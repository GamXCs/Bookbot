"""Delete your "greetings boots" message.
Write a new function called get_book_text(). It takes a filepath as input and returns the contents of the file as a string.
Write a main function that uses get_book_text() with the relative path to your frankenstein.txt file to print the entire contents of the book to the console.
Call main() at the bottom of your file to execute your program.
Test your program!"""

from matplotlib.pyplot import get_backend


def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    text = get_book_text("books/frankenstein.txt")
    print(text[:100])
