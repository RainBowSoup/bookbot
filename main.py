from pathlib import Path
from stats import get_num_words
from stats import num_char
from stats import report
from stats import sort_on
import sys

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        # do something with f (the file) here
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = Path(sys.argv[1])
    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: file not found at {book_path}")
        sys.exit(1)
    return book_text


text = main()
num_words = get_num_words(text)
char_dict = num_char(text)
items = report(char_dict)
items.sort(reverse=True, key=sort_on)

print(f"============ BOOKBOT ============\n"
f"Analyzing book found at {sys.argv[1]}...\n"
f"----------- Word Count ----------\n"
f"{num_words}\n"
f"--------- Character Count -------")
for i in items:
    if i["name"].isalpha():
        print(f"{i['name']}: {i['num']}")
print(f"============= END ===============")