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
        
        