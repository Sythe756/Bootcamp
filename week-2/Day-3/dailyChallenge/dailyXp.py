# Ask ze user for word
user = input("Enter a word: ")

# Convert ze word to smoll leters 
word = user.lower()

# Create ze dic 2 keep ze leter outpu
thedic = {}

# take ze word & store ze leters
for number, letter in enumerate(user):
    if letter not in thedic:
        thedic[letter] = [number]
    else:
        thedic[letter].append(number)

print(thedic)