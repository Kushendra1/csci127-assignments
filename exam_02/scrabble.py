def score(w):
    d = {}
    thescore = 0
    one = "AEIOULNRSTaeioulnrst"
    two = "DGdg"
    three = "BCMPbcmp"
    four = "FHVWYfhvwy"
    five = "Kk"
    eight = "JXjx"
    ten = "QZqz"
    for i in w:
        if i in one:
            d.setdefault(i,0)
            d[i] += 1
            thescore +=1
        elif i in two:
            d.setdefault(i,0)
            d[i] += 2
            thescore +=2
        elif i in three:
            d.setdefault(i,0)
            d[i] += 3
            thescore+=3
        elif i in four:
            d.setdefault(i,0)
            d[i] += 4
            thescore+=4
        elif i in five:
            d.setdefault(i,0)
            d[i] += 5
            thescore+=5
        elif i in eight:
            d.setdefault(i,0)
            d[i] += 8
            thescore+=8
        else:
            d.setdefault(i,0)
            d[i] += 10
            thescore+=10
##    d.setdefault("total", 0)
##    for k in d["total"]:
##        k =
    return thescore
print(score("hello"))
print(score("what"))
        
#----------SOLUTION-----------#
composite_scores = {("A","E","I","O","U","L","N","R","S","T") : 1,
                    ("D", "G") : 2,
                    ("B","C","M","P"): 3,
                    ("F","H","W","Y","V"): 4,
                    ("K"): 5,
                    ("J","X"): 8,
                    ("Q","Z"): 10}

def score1(word, scores):
    score = 0
    for letter in word:
        for k in scores:
            if letter in k:
                score = score + scores[k]
    return score

def score2(word,scores_raw):
    scores = {}
    for k in scores_raw:
        for letter in k:
            scores[letter] = scores_raw[k]
    score = 0
    for letter in word:
        score = score + scores[letter]
    return score