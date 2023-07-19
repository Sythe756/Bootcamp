#exercise 1
# number = int(input("Enter a number: "))
# lenght = int(input("Now enter a lenght: "))

# multiple = []

# for i in range(lenght):
#   multiple.append(number * (i+1))

# print(f"number: " , number, "-", "length", lenght, " = ", multiple )

#exercise 2
user_word = input("Enter a word: ")

new_word = user_word[0]

for i in range(1, len(user_word)):
    if user_word[i] != user_word[i - 1]:
        new_word += user_word[i]

print("New word:", new_word)
