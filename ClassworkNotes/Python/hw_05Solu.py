#Mapping- showing the relationship between two functions or lists and maps it onto
#another

def mapsq(l):
    result = []
    for item in l:
        result = result + [item*item]
    return result
l = [1,2,3,4,3,2,1]

print(mapsq(l))

def filter_odd(l):
    result = []
    for item in l:
        if item %2 !=0 :
            result.append(item)
    return result

print(filter_odd(l))

def filter_even(l):
    result = []
    for item in l:
        if item %2 ==0 :
            result.append(item)
    return result

print(filter_even(l))

def is_odd(n):             #This is a predicate function, same for odd and big.
    return n%2==1

def is_even(n):
    return n%2==0

def is_big(n):
    return n>5

def myfilter(predicate,l):
    result=[]
    for item in l:
        if predicate(item):
            result.append(item)
    return result

print(myfilter(is_odd, l))

def make_upper(w):
    return w[0].upper()+w[1:]

def mymap(f,l):
    result = []
    for item in l:
        result.append(f(item))
    return result

sentence = "when shall we meet again"
print(sentence.split())
print(sentence.split("e"))
wl = sentence.split()
print(" ".join(wl))