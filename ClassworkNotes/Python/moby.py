def build_word_count(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d
            
s = "one two three four five four six three seven three two three eight nine"
print(build_word_count(s))

def clean_data(str):
    result = ""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result = result + letter.lower()
        else:
            result = result + " "
    return result

filename ="moby.txt"
f = open(filename)
s = f.read()
#print(s)
f.close
words_uncleaned = build_word_count(s)
#print(words_uncleaned)
cleaned_string = clean_data(s)
print("--------------------")
words = build_word_count(cleaned_string)
print(words)
vals = words.values()
vals = sorted(vals)
print(vals)

common = []
for k in words:
    if words[k] > 1000:
        common.append([k,words[k]])

uk = []
for k in words:
    if k == "moist":
        uk.append(k, words[k])
        print(uk)
##filename2 = "moby-medium.txt"
##f2 = open(filename2)
##s2 = f2.read()
###print(s2)
##f2.close
##words_uncleaned2 = build_word_count(s2)
###print(words_uncleaned2)
##cleaned_string2 = clean_data(s2)
##print("--------------------")
##words2 = build_word_count(cleaned_string2)
##print(words2)
##
##filename3 = "moby-large.txt"
##f3 = open(filename3)
##s3 = f3.read()
###print(s3)
##f3.close
##words_uncleaned3 = build_word_count(s3)
###print(words_uncleaned3)
##cleaned_string3 = clean_data(s3)
##print("--------------------")
##words3 = build_word_count(cleaned_string3)
##print(words3)