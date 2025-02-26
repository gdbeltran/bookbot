from stats import num_words
from stats import num_characters
from stats import sorted_list
import sys

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()    
    
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents = get_book_text(sys.argv[1])
    count = num_words(contents)
    character_count = num_characters(contents)
    sorted_character_count = sorted_list(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for character in sorted_character_count:
        if list(character.keys())[0].isalpha():
            print(f"{list(character.keys())[0]}: {list(character.values())[0]}")
    
main()