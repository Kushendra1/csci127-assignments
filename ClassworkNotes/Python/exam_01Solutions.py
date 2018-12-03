#                        Compress solution

def compress(word):
    first = word[0]
    rest = word[1:]
    new_rest = ""
    vowels = ["A","E","I","O","U","a","e","i","o","u"]
    for letter in rest:
        if letter not in vowels:
            new_rest = new_rest + letter
    return first + new_rest
print(compress("Testing this function"))

