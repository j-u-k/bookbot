from stats import word_count
from stats import char_count
import sys

if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    word_counter = word_count()
    char_counter = char_count()

    print (f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {word_counter} total words
--------- Character Count -------""")

    for character in char_counter:
        if character["char"].isalpha():
            print (f"{character['char']}: {character['num']}")

    print ("============= END ===============")

    return

main()
