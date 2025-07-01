from stats import get_num_of_words
from stats import get_num_of_characters
from stats import dict_to_list

def get_book_text(filePath):
        bookContents = ""

        with open(filePath) as f:
            bookContents = f.read()

        return bookContents

def sort_on(items):
    return items["count"]

def main():
    numWords = get_num_of_words(get_book_text("books/frankenstein.txt"))
    print(f"{numWords} words found in the document")
    charactersDict = get_num_of_characters(get_book_text("books/frankenstein.txt"))
    #print(characters)
    listOfCharDicts = dict_to_list(charactersDict)
    listOfCharDicts.sort(reverse=True, key=sort_on)
    for item in listOfCharDicts:
        print(f"{item["char"]} : {item["count"]}")



main()

