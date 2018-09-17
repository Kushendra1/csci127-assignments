#Kushendra Ramrup and Madison Chen worked on this
def part_pig_latin(name):
    vowels = ("a","e","i","o","u", "A", "E", "I", "O", "I")
    first_letter = name[0]
    if first_letter in vowels:
        return (name + "ay")
    else:
        return name[1:] + name[0] + "ay"    
    
print(part_pig_latin("Madison"))
print(part_pig_latin("Allison"))
