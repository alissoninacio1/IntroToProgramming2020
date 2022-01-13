# the initial exercise
"""
x = int(input("Enter a number to count to: "))
if x <= 0:
  

# I put 'x + 1' (the last item is not included)so, I can count from 1 to number declared
for i in range(1, x + 1): 
  print i

print "\nNow we will count down\n"
  
count = x

while True:
  print count
  count -= 1
  if count < 1:
    break

"""
print "Please, write a valid score between 0 and 100"


#a function model loop in case of writing a non-integer number
"""
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break
""" 


avSum = 0 #this will be to get a sum of all scores

count = 1 # to count the numbers from 1 to 5 and have 5 prompts to user

#below I put to different cases... in case it is not a integer and invalid caracther. 

while count <= 5:
  try:
    score = int(input("\nWhat was your score: "))
  except ValueError:
    print "\nThis is not a integer"
    
    continue
  
  if score < 0 or score > 100:                   #In case of invalid caracther
    print "\nInvalid score! Please, try again...\n"
    
    continue
  
  count += 1    #this is to increase the loop until five.
  avSum = avSum + score #Now I'm going to sum my scores
 
#my scores average

grade = avSum / 5    #I'll use this fragment to call the function using the scores average

def get_grade(grade): #this is the code from the last week to check the grade according the score
  if 93 <= grade <= 100:
    return "A"
  elif 90 <= grade < 93:
    return " A-"
  elif 87 <= grade < 90:
    return "B+"
  elif 83 <= grade < 87:
    return "B"
  elif 80 <= grade < 83:
    return "B-"
  elif 77 <= grade < 80:
    return "C+"
  elif 73 <= grade < 77:
    return "C"
  elif 70 <= grade < 73:
    return "C-"
  elif 67 <= grade < 70:
    return "D+"
  elif 63 <= grade < 67:
    return "D"
  elif 60 <= grade < 63:
    return "D-"
  else:
    return "F"
    
print "\nFor an average score of " + str(grade) + ", your grade is  " + str(get_grade(grade))
