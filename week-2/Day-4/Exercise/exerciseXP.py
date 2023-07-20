# EX1
import random


def display_message():
    print("I'm learning this code.")


display_message()

# EX2


def favorite_book(title):
    print("One of my favorite books is " + title)


favorite_book("twelth night")

# EX3


def describe_city(city="London", country="United Kingdom"):
    print(f"{city} is in {country}")


describe_city()

# EX4


def random1(x):
    if 1 <= x <= 100:
        y = random.randint(1, 100)
        if x == y:
            print("Yay! you guessed the right number!")
        else:
            print(
                f"Nope, better luck next time.My number was {y} and yours was {x}")
    else:
        print("Try again")


random1(6)

#EX5

def make_shirt(size="large",text="I Love Python"):
  print(f"So your size is {size} and the text on your shirt will be {text}")

make_shirt("small","hello")

#EX6
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians():
#   for x in range(len(magician_names)):
#     print(magician_names[x])

# def make_great():
#   for y in range(len(magician_names)):
#     magician_names[y] = "the Great " + magician_names[y]

# print("Original Magicians:")
# show_magicians()
# make_great()
# print("Magicians with 'the Great' added:")
# show_magicians()

# #EX7
# def get_randm_temp(season):
#   y = {
#         'winter': (-10, 16),
#         'spring': (5, 25),
#         'summer': (20, 40),
#         'autumn': (10, 30)
#     }
#   if season.lower() in y:
#         lower_limit, upper_limit = y[season.lower()]
#   return random.randint(lower_limit, upper_limit)

# def main():
#     season = input("Enter the current season (winter, spring, summer, or autumn): ")
#     temperature = get_randm_temp(season)
#     print(f"The temperature right now is {temperature} degrees Celsius.")
#     if temperature <= 0:
#       print("brr, if you want to turn to ice go outside")
#     elif temperature <= 16:
#       print("Quite chilly! Don’t forget your coat")
#     elif temperature <= 23:
#       print("the perfect day to go out")
#     elif temperature <= 32:
#       print("Turn the air conditioner on because you will be sweating a lot today")
#     else:
#       print("If you don't use sunscreen, you will be returning home with a lot of sun burns")

# main()


#EX5(starwars)
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
