#EX1
# Data Types

#     Which of the following is not a mutable data type in Python?
#     a) List
#     b) Dictionary
#     c) Tuple
#     d) Set

#Ans: (c)



# =========================================================================


# Lists and Loops

#  (i)   Using a list comprehension, generate a list of the squares of numbers from 1 to 10, but only include squares of even numbers.

square= [
  x**2
  for x in range(1, 11)
  if x % 2 == 0
]
print(square)

#     Using the range function, create a list of numbers from 1 to 10, then print numbers that are divisible by both 2 and 3.
num = [
  x for x in range(1, 11)
  if x % 2 == 0 and x % 3 == 0
  ]
print(num)
#     Loop through the provided list of dictionaries and print the names and ages:

student_list = [
    {
    "name": "John", 
    "age": 24
    }, 
    {
    "name": "Anna", 
    "age": 22
    }, 
    {
    "name": "Mike", 
    "age": 25
    }
]
for x in student_list:
    print(x["name"], x["age"])


#==========================================================================


#args and kwargs
# Function Behavior with *args and **kwargs

#     Write a function combine_words that accepts any number of positional argument and key-value argument. The function should return a single sentence combining all the words provided.
#     Example:

# print(combine_words("Hello", "world", second="is", third="great!", first="Python"))

# Expected Output:

# "Hello world. Python is great!"

def combine_words(*args,**kwargs):
  sentence = ""
  for argument in args:
    sentence += " " + argument
  
  for key, value in kwargs.items():
    sentence += " " + value
  return sentence

print(combine_words("Hello", "world", second="is", third="great!", first="Python"))

# Object-Oriented Programming (OOP)

#     Create a class Vehicle with string attributes type, brand, and integer attribute year. Ensure instances of the vehicle cannot be created if any of these attributes are missing and include a method to display the vehicle’s info. Use dunder method.

class Vechicle:

  def __init__(self, type, brand, year):
    """
    Purpose: Ensure instances of the vehicle cannot be created if any of these attributes are missing and include a method to display the vehicle’s info. Use dunder method.
    """
    self.type = type
    self.brand = brand
    self.year = year
  # OOP Inheritance and Decorators
  #     Create a class Car with string attributes brand, model, and integer attribute mileage. Implement a method to return the car’s details.

class Car:
  def __init__(self):
    pass


#     Create a subclass ElectricCar inheriting from Car with an additional float private attribute __battery_capacity. Override the car’s details method to include the battery capacity.
#     Use the @property decorator to get the battery_capacity value and @battery_capacity.setter to modify the battery capacity only if the new value is positive.

#     Create a BankAccount class with private float attribute _balance and private string attribute _account_holder. Implement methods to deposit, withdraw, and view the balance. Include a class method to track accounts created and a static method for a bank policy message. Ensure the balance is non-negative.
