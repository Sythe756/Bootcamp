# # #Exercise 1
# list1 = ["ash","anas"]
# list2 = ["Ash","Anas"]
# for x in list2:
#   list1.append(x)
# print(list1)

# # #Exercise 2
# for num in range(1500,2501):
#   if num % 5 == 0 or num % 7 == 0:
#     print(num)

# # #Exercise 3
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# user = input("Enter your name: ")
# x = names.index(user)
# print(f"You are {x}")

# #Exercise 4
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))
# i = max(num1, num2 , num3)
# print(i)

# #Exercise 5
# alphabets = ["abcdefghijklmnopqrstuvwxyz"]

# def checkForVowelOrConsonent(letter):
#   vowel = "aeiou"
#   if letter in alphabets.lower(vowel):
#     return "vowel"
#   else:
#     return "consonent"

# for letter in alphabets:
#   print(f"{checkForVowelOrConsonent} is a {letter}")

# #EX 6

# user = input("Please enter 7 words: ")
# words = user.split()
# user2 = input("now enter a letter ex. 'a': ")
# letters = user2[0]

# for x in words:
#   if letters in x:
#     print(f"'{letters}' is in the word '{x}' at index {x.index(letters)}.")
#   else:
#     print(f"'{letters }' is not in the word '{x}'.")

# #EX7
# # Create a list of numbers from one to one million
# numbers = list(range(1, 1000001))

# # Use min() and max() to verify the range
# min_number = min(numbers)
# max_number = max(numbers)

# print("Minimum number in the list:", min_number)
# print("Maximum number in the list:", max_number)

# # Use sum() to calculate the sum of a million numbers
# sum_of_numbers = sum(numbers)
# print("Sum of a million numbers:", sum_of_numbers)

