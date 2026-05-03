from collections import defaultdict

"""Write a new function that accepts the text from the book as a string, and returns the number of words in the string."""


def num_of_words(book_text):
    words = book_text.split()

    word_count = len(words)
    return f"Found {word_count} total words"


"""Create function that counts all characters in book & make all lowercase. Return in a dictionary"""


def num_of_chars(book_text):
    char_count = defaultdict(int)

    for char in book_text.lower():
        char_count[char] += 1
    return char_count
