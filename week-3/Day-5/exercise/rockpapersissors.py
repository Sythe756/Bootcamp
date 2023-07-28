print("|------------------------------------------------------------------------|")
print("|~~~~~~~~~~~~~~~~~~~~Welcome to Rock, Paper & Scissors~~~~~~~~~~~~~~~~~~~~|")
print("|------------------------------------------------------------------------|")

player1_name = input("Player 1 enter your name: ")
player2_name = input("Player 2 enter your name: ")


player1 = input(f"{player1_name} enter either rock, paper, or scissors: ")
player2 = input(f"{player2_name} enter either rock, paper or scissors: ")



win_possibs = [["rock","scissors"],["paper","rock"],["scissors","paper"]]

while True:
  if player1 == player2:
    print("Draw")
  else:
    for possibility in win_possibs:
      if [player1, player2] in win_possibs:
        print(f"{player1_name} won")
        break
      else:
        print(f"{player2_name} won")
        break
    quit = input("(q)uit or (p)lay again: ")
    if quit == "q":
      print("Thank you for playing, Ba-Bye!")
      break
    else:
      player1 = input(f"{player1_name} enter either rock, paper, or scissors: ")
      player2 = input(f"{player2_name} enter either rock, paper or scissors: ")

