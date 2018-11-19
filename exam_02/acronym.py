def makeacronym(w):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    n = []
    w = w.lower()
    for k in w.split():
        n.append(k[0])
        if w[k] != alpha:
            n.append(w[k+1])
            break
    return n

print(makeacronym("laugh out loud"))
print(makeacronym("in my opinion"))

