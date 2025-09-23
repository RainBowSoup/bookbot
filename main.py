from pathlib import Path
from stats import get_num_words
from stats import num_char
from stats import report
from stats import sort_on

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        # do something with f (the file) here
        file_contents = f.read()
    return file_contents

def main():
    script_dir = Path(__file__).parent
    book_path = script_dir / "books" / "frankenstein.txt"
    # print(f"book path: {book_path}")
    text = get_book_text(book_path)
    # print(text)
    return text

text = main()
num_words = get_num_words(text)
char_dict = num_char(text)
items = report(char_dict)
items.sort(reverse=True, key=sort_on)

print(f"============ BOOKBOT ============\n"
f"Analyzing book found at books/frankenstein.txt...\n"
f"----------- Word Count ----------\n"
f"{num_words}\n"
f"--------- Character Count -------")
for i in items:
    if i["name"].isalpha():
        print(f"{i['name']}: {i['num']}")
print(f"============= END ===============")