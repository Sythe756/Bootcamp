import random
string = input("The string must be 10 characters long: ")

if len(string) < 10:
  print("string not long enough")
elif len(string) > 10:
  print("string too long")
elif len(string) == 10:
  print("perfect string")

first_character = string[0]
last_character = string[-1]
print("First Character:" , first_character)
print("Last Character:", last_character)

for i in range(len(string)):
  print(string[0:i+1])

s_shuffle= ''.join(random.sample(string, len(string)))
print(s_shuffle)
