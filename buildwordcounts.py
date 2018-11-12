def build_word_count(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d
            
s = "one two three four five four six three seven three two three eight nine"
print(build_word_count(s))

def clean_data(str):
    result = ""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result = result + letter.lower()
        else:
            result = result + " "
    return result


filename ="macbeth.txt"
f = open(filename)
s = f.read()
print(s)
f.close
words_uncleaned = build_word_count(s)
print(words_uncleaned)
cleaned_string = clean_data(s)
print("--------------------")
words = build_word_count(cleaned_string)
print(words)

filename2 = "/home/kushendra/fall-2018-127/classcode/dictionaries/moby.txt"
moby_open = open(filename2)
moby_read = moby_open.read()
build_word_count(moby_read)
clean_data(moby_read)

filename3 = "/home/kushendra/fall-2018-127/classcode/dictionaries/psalms.txt"
psalms_open = open(filename3)
psalms_read = psalms_open.read()
build_word_count(psalms_read)
clean_data(psalms_read)

filename4 = "/home/kushendra/fall-2018-127/classcode/dictionaries/dracula.txt"
drac_open = open(filename4)
drac_read = drac_open.read()
build_word_count(drac_read)
clean_data(drac_read)

filename5 = "/home/kushendra/fall-2018-127/classcode/dictionaries/greatExpect.txt"
great_open = open(filename5)
great_read = great_open.read()
build_word_count(great_read)
clean_data(great_read)