#!/usr/bin/python3

import sys
from stats import get_book_text
from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    
    text = get_book_text(book)
    num_words = get_num_words(book)
    chars = get_num_chars(book)
    sorted_list = get_sorted_list(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_list:
        print(f"{char}: {count}")
    print("============= END ===============")

main()