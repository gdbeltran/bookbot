from stats import num_words
from stats import num_characters

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()    
    
    return contents

def main():
    contents = get_book_text("books/frankenstein.txt")
    count = num_words(contents)
    character_count = num_characters(contents)
    print(f"{count} words found in the document")
    print(f"Character count: {character_count}")
    
main()