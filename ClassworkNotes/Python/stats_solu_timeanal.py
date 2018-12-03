import random

def build_random_list(size, max_value):
    l = []
    i= 0
    while i < size:
        l.append(random.randrange(0,max_value))
        i = i+1
    return l

def max(l):
    x = 0
    large = l[x]
    while x < len(l):
        if l[x] > x:
            large = l[x]
        x += 1
    return large

def freq(l, item):
    count = 0
    for i in l:
        if i == item:
            count = count +1
    return count

def mode(l):
    msf_value = l[0]
    msf_freq = freq(l, l[0])
    msf_index = 0
    for i in range(len(l)):
        test_freq = freq(l, l[i])
        if test_freq > msf_freq:
##            print("Found new possible mode:")
##            print("old mode: ", msf_value, "old freq: ", msf_freq, "old location: ", msf_index)
##            print("new mode : ", l[i], "new freq: ", test_freq, "new location: ", i)
            msf_value = l[i]
            msf_index = i
            msf_freq = test_freq
    return msf_value
                        
mode_test_list = [9,3,3,8,2,8,6,7,8,4,8]
print(mode(mode_test_list))


base_size = 10000
for i in range(1,7):
     l = build_random_list(base_size * i,100)
     #start_time = int(round(time.time() * 1000))
     #m = mode(l)
     #running_time = int(round(time.time() * 1000)) - start_time
     #print("Len: ",len(l), " mode: ",m, "milliseconds: ", running_time)
     start_time = int(round(time.time() * 1000))
     m = fast_mode(l,100)
     running_time = int(round(time.time() * 1000)) - start_time
     print("Len: ",len(l), " mode: ",m, "milliseconds: ", running_time)
     
def fast_mode(l, max_value):
    tallies = []
    for i in range(max_value):
        tallies.append(0)
    print(tallies)
    for item in l:
        tallies[item] = tallies[item] + 1
        li = max(tallies)
    return li

s = build_random_list(105, 15)
print(fast_mode(s, 15))


                    