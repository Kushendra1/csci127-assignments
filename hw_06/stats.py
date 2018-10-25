#Kushendra and Shulamit worked on this

import random

def build_random_list(size, max_value):
    l = []
    i= 0
    while i < size:
        l.append(random.randrange(0,max_value))
        i = i+1
    return l

def largest(l, max):
    print(l)
    i = 0
    while i < len(l):
        if l[i] == max:
            return i
        else:
            i +=1
print(largest(build_random_list(15,11), 10))
            
def freq(l, value):
    print(l)
    count = 0
    for item in l:
        if item == value:
            count +=1
        else:
            pass
    return count

print(freq(build_random_list(15,10), 7))