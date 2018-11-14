#Kushendra Ramrup and Anthony Sokolov

##def build_word_count(words):
##    d={}
##    for word in words.split():
##        d.setdefault(word,0)
##        d[word]=d[word]+1
##    return d
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

def next_word_dict(story):
    d = {}
    s = story.split()
    
    for i in range(len(s)-1):
        d.setdefault(s[i],[])
        d[s[i]].append(s[i+1])
    
    return d

filename ="moby-small.txt"
f = open(filename)
s = f.read()
print(s)
f.close
cleandata = clean_data(s)

next_words = next_word_dict(cleandata)
print(next_words)
