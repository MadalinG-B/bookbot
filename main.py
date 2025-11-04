from stats import *
import sys

def get_book_test(filepath):
    content = ""
    with open(filepath,"r") as f:
        content = f.read()
    
    return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_test(sys.argv[1])
    char_count = get_num_characters(book)
    sort_dict = sort_dic_num(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("--------- Character Count -------")
    for element in sort_dict:
        print(f"{element["char"]}: {element["num"]}")
    print("============= END ===============")
main()
