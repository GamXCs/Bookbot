from stats import num_of_words, num_of_chars, report
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


"""Create function to read a file"""
def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()



if __name__ == "__main__":
    text = get_book_text(sys.argv[1])
    book_path = sys.argv[1]
    print(text[:100] + "\n")

    print(num_of_words(text + "\n"))

    print(num_of_chars(text))

    print(report(text, book_path))
