import random

sentence = "<First_Name> Reeves, whose name means <Adjective> <Noun> over the <Noun> in Hawaiian, <Verb> for a living."
sentence2 = "<Hero> <Verb> in the <Noun> and then <Hero> <Verb> the <Noun> later."

First_Name = ["Keanu", "Charles", "Agatha", "Leslie"]
Adjective = ["dead", "metal", "massive", "blue"]
Noun = ["tank", "sky", "kitty", "jaguar", "mountain", "karate", "weeds", "wolf"]
Verb = ["meditates", "acts", "jumps", "explodes", "ate", "ran"]
Hero = ["Superman", "Wonder-Woman", "Batman", "Thor", "Spiderman"]

#def madlib_easy(s):
    #for item in s.split():
        #s = s.replace("<First_Name>", random.choice(First_Name))
        #s = s.replace("<Adjective>", random.choice(Adjective))
        #s = s.replace("<Noun>", random.choice(Noun))
        #s = s.replace("<Verb>", random.choice(Verb))
    #return s
#print(madlib_easy(sentence))

def madlibs(s):
    new_sentence = []
    hero_name = random.choice(Hero)
    for item in s.split():
        if item == "<First_Name>":
            new_sentence.append(random.choice(First_Name))
        elif item == "<Adjective>":
            new_sentence.append(random.choice(Adjective))
        elif item == "<Noun>":
            new_sentence.append(random.choice(Noun))
        elif item == "<Verb>":
            new_sentence.append(random.choice(Verb))
        elif item == "<Hero>":
            new_sentence.append(hero_name)
        else:
            new_sentence.append(item)
    return " ".join(new_sentence)

print(madlibs(sentence))
print(madlibs(sentence2))
