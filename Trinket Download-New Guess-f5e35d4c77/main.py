import random
from random import randint

print ("Welcome to the number guessing game!")

the_seed_value = input("Enter random seed: ")
random.seed(the_seed_value)

def runningGuess():
  
  numGuessed = randint(1, 100) 
  
  the_seed_value = numGuessed 
  attempts = 0 
  
  while True:
    attempts += 1 
    guess = int(input("\nPlease enter a guess: "))
   
    if guess > the_seed_value:
      print("Lower")
      
    elif guess < the_seed_value:
      print("Higher")
      
    else:
      print("Congratulations. You guessed it!")
      print("It took you {} guesses.".format(attempts))
      return False
      
def playAgain():
  while not False:
    userCheck = input( "\nWould you like to play again (yes/no)? ")
    if userCheck == "yes":
      runningGuess()
    else:
      print("Thank you. Goodbye.")
      return False
      
runningGuess()
playAgain()
