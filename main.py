def letter_reps(str):
    letters = {}
    for char in str:
        lower = char.lower()
        if lower in letters:
            letters[lower] += 1
        else:
            letters[lower] = 1
    return letters

def sort_on(dict):
    return dict["count"]

def dict_to_list(dict):
    dict_list = []
    ls = list((dict.items()))
    
    for item in ls:
        if item[0].isalpha():
            dict_list.append({'character': item[0], 'count': item[1]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list  
  
def num_words(str):
    words = str.split()
    return len(words)
    
def get_text(path):
    with open(path) as f:
        return f.read()
        
def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_text(book_path)
    print (f"---Begin report of {book_path}---")
    words = num_words(file_contents)
    print(f"{words} words found in this document.")
    letters = letter_reps(file_contents)
    list_dict = dict_to_list(letters)
    
    for item in list_dict:
        print(f" The {item['character']} character was found {item['count']} times.")

main()