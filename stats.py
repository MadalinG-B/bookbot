def sort_on(items):
    return items["num"]

def get_num_words(book):
    return len(book.split())

def get_num_characters(book):
    dict = {}
    for char in book:
        char = char.lower()
        if char in dict:
            dict[char]+=1
        elif char.isalpha() :
            dict[char]=1
    return dict

def sort_dic_num(dic):
    lis = []
    for key in dic:
        lis.append({"char":key,"num":dic[key]})
    lis.sort(reverse=True,key=sort_on)
    return lis
