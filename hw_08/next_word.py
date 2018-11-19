#Kushendra Ramrup and Anthony Sokolov


def build_word_count(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d
##
##s = "one two three four five four six three seven three two three eight nine"
##print(build_word_count(s))

def clean_data(str):
    result = ""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result = result + letter.lower()
        else:
            result = result + " "
    return result

def build_word_list(story):
    d = {}
    s = story.split()
    prev = s[0]

    for nextword in s[1:]:
        d.setdefault(prev,[])
        d[prev].append(nextword)
        prev = nextword

    return d

def build_word_list_by_index(story):
    d = {}
    s = story.split()

    for i in range(0,len(s)-2):
        d.setdefault(s[i],[])
        d[s[i]].append(s[i+1])

    return d

def build_word_list_tuple(words):
    d=()
    words = s.split()
    first = words[0]
    second = words[1]
    for next in words[2:]:
        key (first,second)
        d.setdefault(key, [])
        d[key].append(nextword)
        first = second
        second = next_word
    return d

import random
def gen_text(wl,number,startword):
    next = startword
    text = []
    for i in range(number):
        text.append(next)
        next = random.choice(wl[next])
    return " ".joint(text)

def gen_text_tuple(wl,number,tuple):
    first  = tuple[0]
    second = tuple[1]
    text=[]
    for i in range(number):
        text.append(first)
        next = random.choice(wl[tuple])
        tuple = (second,next)
        first = second
        second = next
    return ' '.join(text)


filename ="moby-small.txt"
f = open(filename)
s = f.read()
#print(s)
f.close
cleandata = clean_data(s)

next_words = build_word_list_by_index(cleandata)
print(next_words)
print(build_word_list(cleandata))

wl = build_word_count(cleandata)
wl2 = build_word_list(cleandata) 
