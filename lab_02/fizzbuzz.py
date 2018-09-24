#Kushendra Ramrup worked on this. Darren Zou was not here.

# Go through all the numbers and if the number is divisible by 3 it will print out “Fizz”
#if it’s divisible by 5 it will print out “Buzz” and if divisible by both it will print
#out “FIZZBUZZ”

def fizzbuzz(max_value):
    count = 0
    for i in range(1, max_value+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            count += 1
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 != 0 and i % 5 != 0:
            print(i)
    return print("The string FizzBuzz has appeared", count, "amount of times.")

fizzbuzz(100)
