# #exercise 1
# my_fav_numbers = {35,85,97}

# my_fav_numbers.add(25)
# my_fav_numbers.add(59)

# print(my_fav_numbers)

# my_fav_numbers.remove(59)

# print(my_fav_numbers)

# friend_fav_numbers = {16,2003,12}

# our_favorite_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_favorite_numbers)

# #Exercise 2
# #nope you cannot add nor remove

# #exercise 3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.pop(0)
# basket.pop(-1)
# basket.append("Kiwi")
# basket.insert(0,"Apples")
# apples = basket.count("Apples")
# print(apples, " apples")
# del basket[:]

# print(basket)

# #exercise 4
# #floats display number and its decimal integer doesnt display decimals
# num = []
# for x in range(3,12):
#   num.append(x / 2)
# print(num)

# #exercise 5
# # for x in range(1,21):
# #   print(x)

# for x in range(1,21):
#   if x % 2 == 0:
#     print(x)


# #exercise 6
# # myname = "Anas"
# # while True:
# #   user = input("Enter ya name: ")
# #   if user == myname:
# #     print("Success")
# #     break
# #   elif user != myname:
# #     print("nope")

# #exercise 7
# # user = input("state your favorite fruit(one or several fruits) also space your fruits like this 'apple mango cherry': ").split()
# # print(user)
# # otf = input("name a fruit: ")
# # if otf in user:
# #   print("“You chose one of your favorite fruits! Enjoy!”")
# # else:
# #   print("“You chose a new fruit. I hope you enjoy”")

# # exercise 8
# toppings = []
# total_price = 10
# while True:
#   topping = input("add your toppings'enter quit when you are done': ")
#   if  topping.lower() == "quit":
#     break
#   toppings.append(topping)
#   total_price += 2.5 
#   print(f"Adding {topping} to your pizza")

# print("Topping on your pizza: ")
# for topping in toppings:
#   print(topping)

# print(f"Total price: ${total_price}")

#exercise 9

total_cost = 0
family = []
while True:
  age = input("Enter your age(or type `done` if finished): ")
  if age.lower() == "done":
      break
  age = int(age)
  if age < 3:
      ticket_cost = 0
  elif age >= 3 and age <= 12:
      ticket_cost = 10
  else:
      ticket_cost = 15
  family.append((age, ticket_cost))
  total_cost += ticket_cost
  
print(f"total cost of all tickets: ${total_cost}")

