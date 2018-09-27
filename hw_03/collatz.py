#Kushendra Ramrup and Sam Ebersole

def collatz(n):
    count = 0
    while n != 1:
        if n%2 == 0:
            n = n/2
        else:
            n = (3*n) + 1
        print(n)
        count +=1
    return "The number of steps is "+ str(count)

print(collatz(7))