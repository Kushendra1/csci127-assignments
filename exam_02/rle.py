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