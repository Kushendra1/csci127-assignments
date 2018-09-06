def greeter(name):
    return "Hello " +name+"!"



def hello_name(name):
  return "Hello "+name+"!"
def make_abba(a, b):
  return a+b+b+a
def make_tags(tag, word):
  return "<"+tag+">" + word + "</"+tag+">"

print(hello_name("Bob"))
print(make_abba("Hello","World"))
print(make_tags("i", "Yay"))

