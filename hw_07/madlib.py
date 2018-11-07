import random

sentence = "<First_Name> Reeves, whose name means <Adjective> <Noun> over the <Noun> in Hawaiian, <Verb> for a living."
sentence2 = "<Hero> <Verb> in the <Noun> and then <Hero> <Verb> the <Noun> later."
sentence3 = "<First_Name> eats a <Adjective> <Noun> before he goes to <Noun> . It was there, where he encountered his enemy <Hero> , and then <Verb> for the entire day."

d= {}
d["First_Name"] = ["Keanu", "Charles", "Agatha", "Leslie"]
d["Adjective"] = ["dead", "metal", "massive", "blue"]
d["Noun"] = ["tank", "sky", "kitty", "jaguar", "mountain", "karate", "weeds", "wolf"]
d["Verb"] = ["meditates", "acts", "jumps", "explodes", "ate", "ran"]
d["Hero"] = ["Superman", "Wonder-Woman", "Batman", "Thor", "Spiderman"]

def madlibs(s):
    new_sentence = []
    hero_name = random.choice(d["Hero"])
    for item in s.split():
        if item == "<First_Name>":
            new_sentence.append(random.choice(d["First_Name"]))
        elif item == "<Adjective>":
            new_sentence.append(random.choice(d["Adjective"]))
        elif item == "<Noun>":
            new_sentence.append(random.choice(d["Noun"]))
        elif item == "<Verb>":
            new_sentence.append(random.choice(d["Verb"]))
        elif item == "<Hero>":
            new_sentence.append(hero_name)
        else:
            new_sentence.append(item)
    return " ".join(new_sentence)

print(madlibs(sentence))
print(madlibs(sentence2))
print(madlibs(sentence3))