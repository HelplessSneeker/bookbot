import sys
from stats import word_count, symbol_count, sort_symbols

def get_book_text(filepath):
    file_content = ""

    with open(filepath) as f:
        file_content = f.read()

    return file_content

def main():

    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = word_count(text)
    symbols = symbol_count(text.lower())
    sorted_symbols = sort_symbols(symbols)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for dict in sorted_symbols:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()