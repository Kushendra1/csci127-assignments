# Kushendra Ramrup and Sam Ebersole

def mysqrt(target):
    guess = 1
    while round(guess*guess, 5) != target:
        guess = (guess + (target/guess)) / 2
        print(guess)
    return "The square root of " + str(target) + " is " + str(round(guess, 5))

print(mysqrt(20))
print(mysqrt(25))