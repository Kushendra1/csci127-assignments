# Kushendra Ramrup and Sam Ebersole

def mysqrt(target):
    guess = 1
    while round(guess*guess, 5) != target:
        guess = (guess + (target/guess)) / 2
        print(guess)
    return "The square root of " + str(target) + " is " + str(round(guess, 5))

#print(mysqrt(20))
#print(mysqrt(25))


#Professor Zamansky solution
def calc_new_guess(n,oldguess):
    newguess = (oldguess + ( n / oldguess)) / 2
    return newguess
def zsqrt(n):
    guess = 1
    while abs((guess*guess) - n) > .000001:
        guess = calc_new_guess(n,guess)
    return guess

print(zsqrt(4))
print(zsqrt(20))