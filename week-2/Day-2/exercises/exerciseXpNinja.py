#EX1
import math

C = 50
H = 30
user = input("Please enter a comma-separated string of numbers: ")

numbers = user.split(",")

numbers = [int(num) for num in numbers]

Q = [(2 * C * D) // H for D in numbers]
result_str = ','.join(str(value) for value in Q)
print(result_str)
