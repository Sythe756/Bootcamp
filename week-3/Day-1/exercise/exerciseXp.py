#EX1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
cat1 = Cat("Whiskers", 5)
cat2 = Cat("Fluffy", 3)
cat3 = Cat("Spike", 7)
def oldest_cat(list):
  old_cat = list[0]
  for cat in list:
    if cat.age > old_cat.age:
      old_cat = cat
  return old_cat
calculation = oldest_cat([cat1,cat2,cat3])
print(calculation.age)
print(calculation.name)
print(f"The oldest cat is {calculation.name}, and is {calculation.age} years old.")
#🌟Exercise 2:Dogs
class Dog:
  def __init__(self,name,height):
    self.name = name
    self.height = height
  def bark(self):
    print(f"{self.name} goes: Woof!~")
  def jump(self):
    x = self.height * 2
    print(f"{self.name} jumps {x}cm high")
def biggestDog(list):
  big_dog = list[0]
  for dog in list:
    if dog.height > big_dog.height:
      big_dog = dog
  return big_dog
dog1 = Dog("pakodi",2)
dog1.bark()
dog1.jump()
davidDog = Dog('Rex',50)
davidDog.bark()
davidDog.jump()
sarahDog = Dog('teacup',20)
calculation = biggestDog([dog1,davidDog,sarahDog])
print(calculation.height)
print(calculation.name)
print(f"The biggest dog is {calculation.name}, and is {calculation.height}cm.")
# 🌟 Exercise 3 : Who’s the song producer?

