def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents[:500])
        frankenstein = file_contents.split()
        return len(frankenstein)
main()

print(main())

def count_letters(text):
    letter_dictionary = {}
    for character in text:
        if character.isalpha():
            if character in letter_dictionary:
                letter_dictionary[character] += 1
            else:
                letter_dictionary[character] = 1
    return letter_dictionary

def sort_on(text):
    letters = {}
    for character in text:
        if character.isalpha():
            letters[character.lower()] = letters.get(character.lower(), 0) + 1
    return letters


with open("books/frankenstein.txt") as f:
    file_contents = f.read().lower()
    letter_dictionary = count_letters(file_contents)
    print(letter_dictionary)