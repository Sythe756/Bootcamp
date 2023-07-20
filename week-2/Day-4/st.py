def calculator(a,b):
  add = a+b
  print(f"{a} + {b} = {add}")
  sub = a-b
  print(f"{a} + {b} = {sub}")
  div = a/b
  print(f"{a} / {b} = {div}")
  mul = a*b
  print(f"{a} * {b} = {mul}")
  return (add,sub,div,mul)


res = calculator(40,10)
print(f"so the addition, subtraction, multiplication and division of your numbers is {res}")

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

filtered = list(filter(lambda name: len(name) <= 4,people))
filtered = list(map(lambda name: 'hello ' + name,filtered))
print(filtered)