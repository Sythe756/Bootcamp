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

for string in string:
  print(string)
