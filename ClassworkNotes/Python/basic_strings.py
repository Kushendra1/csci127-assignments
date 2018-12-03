def bondify(name):
    """
    takes in a string in the form "first last" and returns it in the form "last, first last"
    """
    space_index = name.find(" ")
    first = name[0:space_index]
    last = name[space_index:]
    bond_name = last + "," + first + last
    return bond_name

print(bondify("James Bond"))

def capitalize_name(name):
    """
    name -> a string in the form "first last" all lowers case
    returns -> the string with both names capitalized
    ex: james bond -> James Bond
    """
    

s = "Hello World"
print("s = ", s) #adding two strings to put using one argument
print("Access the first character:", s[0]) #printing two seperate strings
#s[0]="Z" this is illegal, you can't change a string
#slices are parts of a string using the character numbers
#You can't change a string, but you can make a new string and reassign the value of s to it

