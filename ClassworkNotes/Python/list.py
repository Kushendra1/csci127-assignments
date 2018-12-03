import random

#create and return a list filled with items number of element
#each element should be a random integer value between 0 and 99

def build_random_list(items):
    i = 0
    while i < items:
        l.append(random.randrange(0,100))
        i = i+1
    return l

l = build_random_list(15,100)
print(l)