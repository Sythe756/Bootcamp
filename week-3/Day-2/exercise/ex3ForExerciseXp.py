from exercisecp import Dog
from random import randint

class PetDog(Dog):
  def __init__(self,name,age,weight):
    super().__init__(name,age,weight)
    self.trained = False
  def train(self):
    print(self.bark())
    self.trained = True
  def doATrick(self):
    """
    Purpose: do a trick
    """
    if self.trained == True:
      print(f"{self.name} does a barrel-roll")
      print(f"{self.name} stands on his back legs")
      print(f"{self.name} shakes your hand")
      print(f"{self.name} plays dead♠")
      return
    else:
      print("Your dog aint trained")
      return
  # end def
  def play(self,*args):
    """
    Purpose: play all together
    """
    print(f"{', '.join(args)} are all together")
  # end def
  def doATrick(self):
    if self.trained == True:
      x = tricks[randint(0,len(tricks)-1)]
      print(self.name,x)
    else:
      print("ya dog aint trained")


tricks = ['does a barrel-roll','stands on his back legs','shakes your hand','plays dead♠']



dog1 = PetDog("ash",18,17,)
dog3 = PetDog("bennet",72,19)
dog1.train()
dog2 = PetDog("charlie",28,10)
dog2.train()
dog1.doATrick()
dog3.doATrick()
dog1.play('charlie','bennet')