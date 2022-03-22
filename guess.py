# number guessing game using python

import random

secret_number = random.randint(1,11) # getting random number
print(secret_number)

lives = 3
score = 0
while lives > 0:
  try:
    user_guess = int(input("Guess a number between 1 - 10 : "))
    if user_guess < 1 or user_guess > 10:
      user_guess = int(input("Guess a number between 1 - 10 : "))
    elif user_guess == secret_number:
      score += 1
      break
    else:
      if abs(secret_number-user_guess) <=2:
        print("You are close. Try again.")
      else:
        print("You are not near. Try again.")
      lives -= 1
  except ValueError as err:
    print("Please enter a number.")
    
if score == 1:
  print(f"You have guessed a secret number {secret_number} correctly.")
else:
  print("You cannot guess it. Try again.")