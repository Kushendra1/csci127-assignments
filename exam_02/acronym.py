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

#print(makeacronym("laugh out loud"))
#print(makeacronym("in my opinion"))

#----------SOLUTION------------#

def make_acronym(line):
    result = ""
    for word in line.split():
        result = result + word[0]
    return result

print(make_acronym("laugh out loud"))
print(make_acronym("in my opinion"))