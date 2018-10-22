def no_vowel(c):
    newstr = ""
    vowels = ('a', 'e', 'i', 'o', 'u')
    for i in c:
        if i in vowels:
            newstr = c.replace(i, "")        
    return newstr
# I made two different functions to help me organize my thoughts better. If that was wrong, I apologize.

def compress_word(w):
    word = w[1:]
    new_word = no_vowel(word)
    return w[0] + new_word

print(compress_word("apple"))
print(compress_word("orange"))

def sentence(line):
    l = []
    for i in line.split():
        if i in line:
            l.append(compress_word(i))
    return " ".join(l)
print(sentence("I like apples"))
