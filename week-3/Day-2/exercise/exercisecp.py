#EX1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

Bengal = Cat("whiskers",99)
Chartreux = Cat("soz",29)
Siamese = Cat("soz numero 2",92)
allCats = [Bengal,Siamese,Chartreux]

saraPets = Pets(allCats)

saraPets.walk()





#EX2
class Dog():
  def __init__(self,name,age,weight):
    self.name = name
    self.age = age
    self.weight = weight
  def bark(self):
    """
    Purpose: name of the dog barks
    """
    return f"{self.name} goes woof!~"
  # end def
  def run_speed(self):
    """
    Purpose: dog go brrrr
    """
    return self.weight / self.age * 10
  # end def
  def fight(self,otherDog):
    """
    Purpose: dog goes grrrr
    """
    selfSpeed = self.run_speed() * self.weight
    otherDogSpeed = self.run_speed() * otherDog.weight
    if selfSpeed > otherDogSpeed:
      return f"{self.name} won!"
    elif otherDogSpeed < selfSpeed:
      return f"{otherDog.name} won!"
    else:
      return f"Draw!"
  # end def
dog2 = Dog("Xer",34,20009)
dog3 = Dog("Exr", 34 , 200)
mydog = Dog("Rex",34,29)
mydog.bark()
mydog.run_speed()
dog2.bark()
dog2.run_speed()
dog3.bark()
dog3.run_speed()
print(mydog.fight(dog2))
print(dog3.fight(dog2))
print(mydog.fight(dog3))

