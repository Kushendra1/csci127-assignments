def cake_amount(A,B,u):
    while u > 0:
        cake_piece = A/B
        people = int(u/cake_piece)
        return print("Leha should invite",people,"amount of people to his party")

print(cake_amount(5,10,1))
print(cake_amount(5,10,2))
print(cake_amount(3,18,1))

#Cake solution

