def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    letter_count_dict = count_the_letters(text)
    final_sorted_list = final_sort(letter_count_dict)
    print(final_sorted_list)
    


def count_the_words(text):
    words = text.split()
    return len(words)

def count_the_letters(text):
    letter_dictionary = {}
    lowered_string = text.lower()
    for characters in lowered_string:
        if characters.isalpha(): 
            if characters in letter_dictionary:
                letter_dictionary[characters] += 1
            else:
                letter_dictionary[characters] = 1

    return letter_dictionary

def sort_on(dict):
    return dict["num"]

def final_sort(letter_count_dict):
    sorted_list = []
    for character in letter_count_dict:
        sorted_list.append({"letter": character, "num": letter_count_dict[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()