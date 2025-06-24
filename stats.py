def get_book_text (file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count():
    text = get_book_text ("books/frankenstein.txt")
    words = text.split()
    count = len(words)
    return count

def sort_on(characters):
    return characters["num"]

def char_count():
    text = get_book_text ("books/frankenstein.txt")
    lower_text = text.lower()
    character_count = {}
    for character in lower_text:
        if character in character_count:
            character_count[character] +=1
        else:
            character_count[character] = 1
    character_list = []
    for character in character_count:
        number = character_count[character]
        new_dict = {}
        new_dict["char"] = character
        new_dict["num"] = number
        character_list.append(new_dict)
    character_list.sort(reverse=True, key=sort_on)
    return character_list      
