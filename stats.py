import string
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


# helper function to get the value from the dictionary
def sort_dict(book_dict):
    return book_dict["num"]


# helper function to sort the dict by turning it into a list
def char_dict_to_sorted_list(char_dict):
    char_list = []

    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=sort_dict)
    return char_list


"""Generate report"""


def report(book_text, book_path):

    word_count = num_of_words(book_text)
    char_count = num_of_chars(book_text)
    sorted_chars = char_dict_to_sorted_list(char_count)

    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {book_path}...\n")
    print("------------ Word Count ------------\n")
    print(word_count + "\n")
    print("----------- Character Count -----------\n")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============ END ============\n")
