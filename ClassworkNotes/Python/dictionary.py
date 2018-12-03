l= [1,2,"Hello", .34]

#Dictionary is a data structure that allows you to store different types of
#data. Also known as a hash map or key pairs.

#The list above is not a dictionary as only python allows lists to be created
# with more than one type of info.

d={}                            # empty dictionary
d["key1"] = "hello"
d["name"] = "Horatio Hornblower"
d[0] = "hello world"
d[5] = 26
d["float"] = 123.456
d["x"] = [5,2,3,1,6]

person1 = {"name": "tom", "age": 22}
person2 = {"name" : "sally", "age": 18}
person3 = {"name" : "sue", "age": 20}
myage= 19
myname= "albert"
people = {"tom" :person1, "sally" :person2}
people["sue"] = person3

for k in people:
    print(k)

print("--------------")
for k in sorted(people):
    print(k, " is ",people[k]["age"]," years old.")
    

    

