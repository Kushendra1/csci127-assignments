#Kushendra Ramrup

##def addline(d,line):
##    d1 = {}
##    list = []
##    new_line = line.lower()
##    for word in line:
##        if word[0] in d:
##            l.append(word)
##        else:
##            d1[word[0]] = word
##    return d1

def addline(d,line):
    new_line = line.lower()
    letter = new_line[0]
    d1 = {}
##    print(new_line.split())
    for i in new_line.split():
        
    for i in new_line:
        if letter in d.keys():
            d[letter].append(new_line)
        else:
            d1[letter] = [new_line]
    return d1

dict = {"name": "jack", "person": "two"}
print(addline(dict, "name face person"))
dict2 = {"water" : "wet", "earth": "hard", "fire": "hot", "air" : "cool"}
print(addline(dict2, "wind earth fire agua"))

d = addline({}, "string")
d = addline(d, "movie")
d = addline(d, "cars")
d = addline(d, "time")
d = addline(d, "branch")

def spellcheck(d, word):
    new_word = word.lower()
    if new_word[0] in d:
        if new_word in d[new_word[0]]:
            return True
        else:
            return False
    return False

    
    