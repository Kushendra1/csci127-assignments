def count(b):
    d={}
    d["color"] = []
    d["amount"] = []
    for i in b:
        if i != "_":
            if i not in d["color"]:
                d["color"].append(i)
                d["amount"].append(1)
            else:
                d["amount"][d["color"].index(i)]+=1
    return d["amount"]

def happy(l, str):
    if l < 3:
        if l == 1 and str[0] == "_":
            return True
        if l == 2 and str[0] == str[1]:
            return True
        else:
            return False
    elif l >= 3:
        for i in count(str):
            if i < 2:
                return False
        return True
    return True

def HappyLadyBug(n,b):
    if happy(n,b) == False:
        return "No"
    elif happy(n,b) == True:
        return "Yes"
    
print(HappyLadyBug(3, "RB_"))
print(HappyLadyBug(0, ""))