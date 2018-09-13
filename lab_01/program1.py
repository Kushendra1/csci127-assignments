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
def extra_end(str):
  return str[-2:]+str[-2:]+str[-2:]
def first_two(str):
  return str[0:2]
def first_half(str):
  return str[:len(str)//2]
def without_end(str):
  return str[1:-1]
def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  return a + b + a
def non_start(a, b):
  return a[1:] + b[1:]

print(hello_name("Bob"))
print(make_abba("Hello","World"))
print(make_tags("i", "Yay"))
print(make_out_word("<<>>", "Yay"))
print(extra_end("Hello"))
print(first_two("Hello"))
print(first_half("WooHoo"))
print(without_end("Hello"))
print(combo_string("Hello", "Hi"))
print(non_start("python", "code"))