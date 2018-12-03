empty_list=[]
l=[0,10,20,30,40,50,60,70,80,90,100]
l2=[10,"Hello",True,3.5,20]
l3=[16]

s = "Hello World"

#You can index, slice, and add lists just like arrays.

print(len(l))
print(l2)
l2[2]="New String"     #You can reassign a list value
# s[2] = 'a' <--- you can't do this to a string

print(l2)

l3.append(1)
l3.append("word")
l3.append(l2)
print("l3:", l3)

l4= l3+ l2
print("Changing l2[1] to a Z")
l2= "Z"
print("l2:", l2)
print("l4:", l4)

l2.insert(3, "I've been inserted")
print("l2:", l2)
l2.remove(3.5)            #Removes first occurance of 3.5
print("l2:",l2)