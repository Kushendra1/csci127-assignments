
def compress_word(w):
    word = w[1:]
    newstr = ""
    vowels = ('a', 'e', 'i', 'o', 'u')
    for i in w[1:]:
        if i in vowels:
            newstr = w[1:].replace(i, "")
    return w[0] + newstr

print(compress_word("apple"))
print(compress_word("orange"))

def sentence(line):
    l = []
    for i in line.split():
        if i in line:
            l.append(compress_word(i))
    return " ".join(l)
print(sentence("I like apples"))
