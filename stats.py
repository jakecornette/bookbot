def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(book):
    words = book.split()
    word_count = len(words)
    return word_count

def letter_count(book):
    book = book.lower()
    counts = {}
    
    for ch in book:
        if ch.isalpha():  # keep only letters
            if ch not in counts:
                counts[ch] = 0
            counts[ch] += 1              
    return counts

def sort_on(items):
    return items["num"]

def sort_list(list_of_dictionaries):
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return

def convert_to_list(dictionary): #Converts a dictionary to a list of dictionaries with single key:value pairs.
    new_list = []
    for key in dictionary:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dictionary[key]
        new_list.append(new_dict)
    return new_list


