def encode(s):
    d = {}
    for i in s:
        if i not in d:
            d.setdefault(i, 1)
        else:
            d[i] += 1
    return d

print(encode("abbaaacddaaa"))
print(encode("abcd"))

def decode(l):
    n = []
    for item,num in l: 
        new = item*num
        l += new
    return "".join(l)
        
list = ["A", 1]
list2 = ["b", 2]
print(decode(list))
print(decode(list2))
