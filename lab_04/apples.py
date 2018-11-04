s,t = [7,11]
a,b = [5,15]
m,n = [3,2]
apples = [-2,2,1]
oranges = [5,-6]

def countApplesAndOranges(s,t,a,b,m,n):
    final_apples = 0
    final_oranges = 0
    
    for item in apples: 
        if a + item in range(s,t+1):
            final_apples += 1
    for item in oranges:
        if b - item in range(s,t+1):
            final_oranges += 1
    return "Sam's apples are:", final_apples ,"Sam's oranges are:", final_oranges

print(countApplesAndOranges(s,t,a,b,m,n))

