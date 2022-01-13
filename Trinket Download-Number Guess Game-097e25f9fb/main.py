import random

print "To play with this amazing game, write a number between 1 and 75"

n = random.randint(1, 75) # this is the range we need to use in our program

att = 0 #to count the number of attempts
first_att = 1 #this is to sum with the number of attempts we have since the first one

while True:
  
  att += first_att  #I put at the beginning to include in my attempts, the correct attempt
  
  try:    #this is to check if the user wrote a correct character
    guess = int(raw_input("\nEnter an integer from 1 to 75: "))
  except ValueError:
    print "\nThis is not a number or integer"
    
    continue
  
  if guess < 1 or guess > 75:       #this is to check if the user put a valid number
    print "\n Did you write a number between 1 and 75?"
    
    continue  
  
  if guess > n:
    print "\nYour guess is too high"

  elif guess < n:
    print "\nYour guess is too low"
  
  else: #the correct number will be this, because all the previous alternatives are false
    print " You guessed the correct number in %d attempts" % (att)
    break
  
  """my else statement: is the only sentence whose number is not higher than or lower than 
  guess, so I can infer that this is the "guess = random number", thus I break the loop"""
  