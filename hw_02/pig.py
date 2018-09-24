<<<<<<< HEAD
#Kushendra Ramrup and Madison Chen worked
=======
#Kushendra Ramrup and Madison Chen worked on this
>>>>>>> d313b1ffe62ea24d0a43e514df91bdbedca93cb3
def piglatinify(name):
    vowels = ("a","e","i","o","u", "A", "E", "I", "O", "I")
    first_letter = name[0]
    if first_letter in vowels:
        return (name + "ay")
    else:
        return name[1:] + name[0] + "ay"    
    
print(piglatinify("Madison"))
print(piglatinify("Allison"))
<<<<<<< HEAD
print(piglatinify("kush"))
print(piglatinify("eddie"))
=======
>>>>>>> d313b1ffe62ea24d0a43e514df91bdbedca93cb3
