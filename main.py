import stats    
import sys


def main(): 

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)

    book = sys.argv[1]
    text = stats.get_book_text(sys.argv[1])

   # print(f"{stats.get_num_words(text)} words found in the document")

    num_words = stats.get_num_words(text)
    letters = stats.letter_count(text)
    list_of_dicts = stats.convert_to_list(letters)
    list_of_dicts.sort(reverse=True, key=stats.sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for n in range(0, len(list_of_dicts)):
        dictionary = list_of_dicts[n]
        character = dictionary["char"]
        number = dictionary["num"]
        print(f"{character}: {number}")

    
    print("============= END ===============")
         
  

main()

