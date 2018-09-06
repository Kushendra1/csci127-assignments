def greeter(name):
    return "Hello " +name+"!"



def hello_name(name):
  return "Hello "+name+"!"
def make_abba(a, b):
  return a+b+b+a
def make_tags(tag, word):
  return "<"+tag+">" + word + "</"+tag+">"
def make_out_word(out, word):
  return out[0:2]+word+out[-2:]

print(hello_name("Bob"))
print(make_abba("Hello","World"))
print(make_tags("i", "Yay"))
print(make_out_word("<<>>", "Yay"))

