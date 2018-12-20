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





