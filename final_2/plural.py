#Kushendra Ramrup

def countPlurals(line):
    l = line.split()
    count = 0
    for i in l:
        if i[len(i)-1] == 's':
            count += 1
        else:
            continue
    return count
print(countPlurals("dogs cat"))
print(countPlurals("heads shoulder knees toes"))

def notPossesive(line):
    l = line.split()
    count = 0
    for i in l:
        if i[len(i)-1] == 's' and i[len(i)-2] == "'":
            count += 1
        else:
            continue
    return count
print(notPossesive("heads hers adam's gail's"))
print(notPossesive("adam's kim's kevin's dogs"))



