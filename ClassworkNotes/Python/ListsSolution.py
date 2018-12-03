#Zamansky solutions and notes
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
    i = 0
    found_index = -1
    while i < len(l):
        if l[i] == value: #L subzero, allows code to loop through entire list
            found_index = i
            break # breaks out of current loop
        i = i+1
    return found_index

l = build_random_list(15, 100)
print(l)
print(locate(l, 10))
print(locate(l, l[4]))

def count(l, value):
    i = 0
    found_count = 0
    while i < len(l):
        if l[i] == value:
            found_count = found_count+1
        i = i+1
    return found_count

l2 = build_random_list(200, 50)
print(count(l2, l2[4]))

def reverse(l):
    print(l)
    reversed = []
    i = len(l) - 1
    while i >= 0:
        reversed.append(l[i])
        i -= 1
    return reversed
    
print(reverse(l))

def palindrome(l):
    l2 = reverse(l)
    return l == l2
print(palindrome("hello"))
print(palindrome("racecar"))

def isIncreasing(l):
    increasing = True
    i = 0
    while i < len(l)-1:
        if l[i] >= l[i+1]:
            increasing = False
            break
        i = i+1
    return increasing

l = [1,2,3,4]
print(isIncreasing(l))
    