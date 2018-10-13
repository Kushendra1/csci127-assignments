#Kushendra Ramrup
s= [1,2,3,4,5,6,7,8]

def filterodd(l):
    l2 = [] 
    for i in l: 
        if i % 2 == 1: 
            l2.append(i) 
    return l2 
print(filterodd(s))

def mapsquare(l):
    l2 = []
    for i in l:
        i = (i*i)
        l2.append(i)
    return l2
print(mapsquare(s))