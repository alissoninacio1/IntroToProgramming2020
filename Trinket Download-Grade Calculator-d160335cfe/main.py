grade = int(input("Let me know your score, please write a number between 0 and 100:  "))

def get_grade(grade):
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

print "For a score of " + str(grade) + ", your grade is a " + str(get_grade(grade))