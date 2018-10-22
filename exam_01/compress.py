
def compress_word(w):
    word = w[1:]
    newstr = ""
    vowels = ('a', 'e', 'i', 'o', 'u')
    for i in w[1:]:
        if i in vowels:
            newstr = w[1:].replace(i, "")
    return w[0] + newstr
    #new_word = no_vowel(word)
    #return w[0] + new_word

print(compress_word("apple"))
print(compress_word("orange"))

def sentence(line):
    l = []
    for i in line.split():
        if i in line:
            l.append(compress_word(i))
    return " ".join(l)
print(sentence("I like apples"))
