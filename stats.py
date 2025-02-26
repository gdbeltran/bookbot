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