def encode(s):
    d = {}
    d["letter"] = []
    d["amount"] = []
    for i in s:
        if i not in d["letter"]:
            d["letter"].append(i)
            d["amount"].append(1)
        else:
            d["amount"][d["letter"].index(i)]+=1
    return d

print(encode("abbaaacddaaa"))
print(encode("abcd"))