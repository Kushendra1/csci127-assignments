#Kushendra Ramrup
import random
def build_random_list(size, max_value):
    l = []
    i= 0
    while i < size:
        l.append(random.randrange(0,max_value))
        i = i+1
    return l
print(build_random_list(10, 99))

def locate(l, value):
    print(l)
    i = 0
    while i < len(l):
        if l[i] == value:
            return i
        else:
            i+=1
    return -1
print(locate(build_random_list(10, 25), 15))

def count(l, value):
    print(l)
    count = 0
    for i in l:
        if i == value:
            count +=1
    return count
print(count(build_random_list(10,25), 15))

def reverse(l):
    print(l)
    i = len(l)-1
    while i >=0:
        print(l[i])
        i -= 1
print(reverse(build_random_list(10,25)))

s = [1,5,3,5,1]
def isIncreasing(l):
    print(l)
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True
print(isIncreasing(s))

def palindrome(l):
    print(l)
    if l[::-1] == l:
        return True
    return False
print(palindrome(s))
    
    
    





    
