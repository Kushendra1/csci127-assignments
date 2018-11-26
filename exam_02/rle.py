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

#----------SOLUTION-----------#

##def rle1(line):
##    encoded = []
##    i = 0
##    while i < len(line)-1:
##        next_letter = i+1
##        while next_letter < len(line) and line[next_letter] == line[i]:
##            next_letter = next_letter = 1
##        encoded.append(([next_letter-i], line[i]))
##        i = next_letter
##    if i == len(line)-1:
##        encoded.append( [1, line[i]])
##    return encoded
##
##print(rle1("abbaaacddaaa"))
##print(rle1("abcd"))

def rle2(line):
    encoded = []
    count = 1
    prevchar = line[0]
    for c in line[1:]:
        if c==prevchar:
            count = count+1
        else:
            encoded.append([count,prevchar])
            count = 1
            prevchar = c
    encoded.append([count,prevchar])
    return encoded

print(rle2("abbaaacddaaa"))
print(rle2("abcd"))

def dec(encoded):
    result = ""
    for item in encoded:
        result = result + item[0] * item[1]
    return result

print(dec([['a', 1], ['b', 2], ['a', 3], ['c', 1]]))
print(dec([['a', 1], ['b', 1], ['c', 1], ['c', 1]]))
