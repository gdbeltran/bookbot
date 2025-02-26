def num_words(text):
    words = text.split()
    count = len(words)
    
    return count

def num_characters(text):
    count = {}
    words = text.lower()
    for character in words:
        if character in count:
            count[character] += 1
        else:
            count[character] = 1
    
    return count

def sort_on(dictionary):
    return list(dictionary.values())[0]

def sorted_list(dictionary):
    list = []
    for character, count in dictionary.items():
        character_dict = {character: count}
        list.append(character_dict)
    list.sort(reverse=True, key=sort_on)
    return list