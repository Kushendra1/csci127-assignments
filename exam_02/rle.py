##def encode(s):
##    d = {}
##    for i in s:
##        if i not in d:
##            d.setdefault(i, 1)
##        else:
##            d[i] += 1
##    return d
##
##print(encode("abbaaacddaaa"))
##print(encode("abcd"))

def encode(s):
    l = []
    count = 1
    for i in range(0, len(s) - 1):
        if s[i] != s[i + 1]:
            l.append([s[i], count])
            count = 1
        else:
            count += 1
        new = [s[i], count]
    l.append(new)
    return l
    
print(encode("abbaaacddaaa"))
print(encode("abcd"))

def decode(l):
    k = ""
    for i in l:
        k += i[0] * i[1]
    return k

print(decode([['a', 1], ['b', 2], ['a', 3], ['c', 1]]))
print(decode([['a', 1], ['b', 1], ['c', 1], ['c', 1]]))
