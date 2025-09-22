from pathlib import Path

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        # do something with f (the file) here
        file_contents = f.read()
    return file_contents

def num_words(text):
    print(f"Found {len(text.split())} total words")
    return len(text.split())

def main():
    script_dir = Path(__file__).parent
    book_path = script_dir / "books" / "frankenstein.txt"
    # print(f"book path: {book_path}")
    text = get_book_text(book_path)
    # print(text)
    return text

text = main()
num_words(text)
# print(text)
