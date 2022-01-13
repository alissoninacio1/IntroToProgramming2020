import math

def displayWelcome():    # TODO -> Add welcome function here
  print " Welcome to my area and perimeter calculator"
  print 50 * "="

def calcAreaCircle(radius): # TODO -> Add circle area function here
  return math.pi * (radius ** 2)
  
def calcPerimeterCircle(radius):  # TODO -> Add circle perimeter function here
  return math.pi * 2 * radius

  
def calcAreaSquare(side):   # TODO -> Add square area function here
  return side * side
  
def calcPerimeterSquare(side):  # TODO -> Add Square perimeter function here
  return side * 4

  
def calcAreaRect(width, height):    # TODO -> Add rectangle area function here
  return width * height 
  
def calcPerimeterRect(width, height):   # TODO -> Add rectangle perimeter function here
  return (width * 2) + (height * 2)


def calcAreaTriangle(base, height):   # TODO -> Add triangle area function here
  return (base * height) / 2
  
  
# =====================================================================

# Main Code - DO NOT EDIT ANYTHING BELOW.  Add your functions above

displayWelcome()


radius = 3.56

area = calcAreaCircle(radius)

perimeter = calcPerimeterCircle(radius)

print('Circle   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


side = 9.23

area = calcAreaSquare(side)

perimeter = calcPerimeterSquare(side)

print('Square   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


width = 2.9

height = 14.22

area = calcAreaRect(width, height)

perimeter = calcPerimeterRect(width, height)

print('Rectangle: area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


base = 7.97

height = 5.31

area = calcAreaTriangle(base, height)

print('Triangle : area = {0:.2f}'.format(area))
  
