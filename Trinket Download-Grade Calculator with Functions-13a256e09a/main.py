"""in this simple program, I didn't want to use an option to check if the user put a valid input
I only ask to put a valid number. If the program request I can add a try/except to check errors"""

print "Please, you only need to use valid numbers/integers between 0 and 100!"

#here I will prompt the user to enter a numerical score
score_1 = int(input("\nEnter the score you received for Math: "))
score_2 = int(input("Enter the score you received for English: "))
score_3 = int(input("Enter the score you received for PE: "))
score_4 = int(input("Enter the score you received for Science: "))
score_5 = int(input("Enter the score you received for Art: "))

#this function I used in the last lessons, so I'm reusing it. 
def get_score(grade):
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

# Now I'm calling the function and print it at the same time for each score.
print "\nYour Math Score is " + str(score_1) + ", you got a " + str(get_score(score_1))
print "Your English Score is " + str(score_2) + ", you got a " + str(get_score(score_2))
print "Your PE Score is " + str(score_3) + ", you got a " + str(get_score(score_3))
print "Your Science Score is " + str(score_4) + ", you got a " + str(get_score(score_4))
print "Your Art Score is " + str(score_5) + ", you got a " + str(get_score(score_5))