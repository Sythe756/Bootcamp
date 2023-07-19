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