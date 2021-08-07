import random

lb=1
ub=random.randint(20,100)
correct_guess=random.randint(lb,ub)
chances=5

# Game loop
while True:
  if(chances==0):
    print("You have lost and the correct guess was",correct_guess)
    break
  
  print("\n\nGuess a number between",lb,"and",ub)
  print("You have",chances,"chances left")
  guess=int(input("Enter your guess:"))
  
  if(guess==correct_guess):
    print("You have won")
    break
  else:
    if(guess > correct_guess):
      print("Guess lower")
    else:
      print("Guess higher")
    chances=chances-1
    

  