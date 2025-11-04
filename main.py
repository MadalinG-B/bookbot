from stats import *

def get_book_test(filepath):
    content = ""
    with open(filepath,"r") as f:
        content = f.read()
    
    return content

def main():
    book = get_book_test("books/frankenstein.txt")
    char_count = get_num_characters(book)
    sort_dict = sort_dic_num(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("--------- Character Count -------")
    for element in sort_dict:
        print(f"{element["char"]}: {element["num"]}")
    print("============= END ===============")
main()
