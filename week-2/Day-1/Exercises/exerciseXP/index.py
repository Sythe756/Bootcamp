#exercise 1 
print("Hello World!\n" * 5)

#exercise 2
print((99**3)*8)

#exercise 3
print(5 < 3)
#False
print(3 == 3)
#True
print(3 == "3")
#False
# print("3" > 3)
#error
print("Hello" == "hello")
#false

#exercise 4
computer_brand = "dell"
print("I have a, " + computer_brand + " computer.")

#exercise 5
name = "Anas"
age = "17"
shoe_size = "39"
info = "Hello, My name is " + name + " and I am " + age + " years old. My shoe-size is " + shoe_size + " and also " +  "I am short"
print(info)

#exercise 6
a = "34"
b = "24"
if a > b:
  print("Hello World!")
  
#exercise 7
number = int(input("Write a number: "))

if number % 2 == 0:
  print("this is an even number")
if number % 2 != 0:
  print("this is an odd number")
#exercise 8
name = input("Enter you name: ")

if name == "Anas" or "anas" or "rasmally" or "Rasmally":
  print("Yay,we have da same name :>")
else:
  print("Noo, we dont have the same name :<")
  
#exercise 9
height = int(input("Write your name in INCHES: "))

if height >= 57:
  print("You are tall enough to ride.")
else:
  print("You need to grow some more to ride.")