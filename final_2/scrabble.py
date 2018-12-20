#Kushendra Ramrup

def canMakeWord(letters,word):
    for i in letters:
        if letters.count(i) < word.count(i):
            return False
        else:
            continue
    return True
print(canMakeWord("ladilmy","daily"))
print(canMakeWord("eerriinn","eerie"))

def withWild(letters,word):
    wildcard = letters.count("?")
    l = []
    for i in word:
        if i not in l:
            count = letters.count(i)
            if count >= word.count(i):
                continue
            elif count + wildcard >= word.count(i):        
                wildcard = wildcard - (word.count(i) - count)
                l.append(i)
                continue
            else:
                return False
        else:
            continue
    return True
print(withWild("ladi?my", "daily"))
print(withWild("eerrii?nn", "eerie"))