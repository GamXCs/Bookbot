from stats import num_of_words, num_of_chars, report

"""Create function to read a file"""
def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()



if __name__ == "__main__":
    text = get_book_text("books/frankenstein.txt")
    book_path = "books/frankenstein.txt"
    print(text[:100] + "\n")

    print(num_of_words(text + "\n"))

    print(num_of_chars(text))

    print(report(text, book_path))
