#exercise 1
print(("Hello World!\n" * 4) + ("I Love Python\n" * 4))

#exercise 2
month = int(input("Write a month 1-12: "))

if month >= 3 and month <= 5:
  print("it is spring")
elif month >= 6 and month <= 8:
  print("Summer")
elif month >= 9 and month <= 11:
  print("Autumn")
else:
  print("Winter")