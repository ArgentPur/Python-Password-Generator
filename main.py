import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

newLetter = ''
allLetters = ''
for x in range(nr_letters):
  if nr_letters >= 0:
   nr_letters -= 1
   newLetter = letters[random.randint(0, len(letters) - 1)]
   allLetters += newLetter

newNum = ''
allNum = ''
for x in range(nr_numbers):
  if nr_numbers >= 0:
    nr_numbers -= 1
    newNum = numbers[random.randint(0, len(numbers) - 1)]
    allNum += newNum

newSym = ''
allSym = ''
for x in range(nr_symbols):
  if nr_symbols >= 0:
    nr_symbols -= 1
    newSym = symbols[random.randint(0, len(symbols) - 1)]
    allSym += newSym  

simpleNewPass = [allLetters + allNum + allSym]

newList = list(simpleNewPass[0])
newPass = random.sample(newList, len(newList))
newStringPass = ''.join(newPass)

print(f"Your new password is: {newStringPass}")