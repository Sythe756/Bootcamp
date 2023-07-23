#EX 3
# 3 <= 3 < 9

a = 3 <= 3 < 9
print(a)
#true


#>>> 3 == 3 == 3
b = 3 == 3 == 3
print(b)
#true


#>>> bool(0)
c = bool(0)
print(c)
#false


#>>> bool(5 == "5")
d = bool(5 == "5")
print(d)
#false


#>>> bool(4 == 4) == bool("4" == "4")
e = bool(4 == 4) == bool("4" == "4")
print(e)
#true


#>>> bool(bool(None))
f = bool(bool(None))
print(f)
#false


x = (1 == True)
y = (1 == False)
i = True + 4
j = False + 10
print("x is", x)
print("y is", y)
print("i:", i)
print("j:", j)

#x is True . .... . because 1 == True
#y is False . .... . because 1 isnt ==  True but 0 == False
#i: 5 . ... . because True == 1 so 1 + 4 = 5
#j: 10 . ... . because False == 0 so 0 + 10 = 10


#EX4

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))

#EX5 

print("Welcome to write the longest sentence without an 'A'.")
print("Your goal my friend is to type the longest sentence possible without using 'A' and the sentence must make sense.")
print("Goodluck!")
user = input("Enter your sentence right here ---> ")
if 'a' in user:
  print("Nope there is an 'a' in your sentence")
elif 'A' in user:
  print("Nope there is an 'A' in your sentence")
  if len(user) <= 20:
    print(" tho your sentence kinda of a short dont you think?")
  else:
    print("noice long phrase you got")
else:
  print("Congrats! you won a price")
  print("wait for it...")
  print("yay you wont nothing!")
# if len(user) <= 20:
#   print(" tho your sentence kinda of a short dont you think?")
# else:
#   print("noice long phrase you got")