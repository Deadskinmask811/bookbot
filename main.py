from stats import get_num_of_words
from stats import get_num_of_characters
from stats import dict_to_list
import sys

def get_book_text(filePath):
        bookContents = ""

        with open(filePath) as f:
            bookContents = f.read()

        return bookContents

def sort_on(items):
    return items["count"]

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1] 
    numWords = get_num_of_words(get_book_text(filepath))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {numWords} total words")
    print("--------- Character Count -------")
    charactersDict = get_num_of_characters(get_book_text("books/frankenstein.txt"))
    #print(characters)
    listOfCharDicts = dict_to_list(charactersDict)
    listOfCharDicts.sort(reverse=True, key=sort_on)
    for item in listOfCharDicts:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")

    print("============= END ===============") 

main()

