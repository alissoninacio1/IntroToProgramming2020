shape = raw_input("Enter C for Circle, T for Triangle, or R for Rectangle: ")

if shape == "C":
  radius = float(raw_input("Enter the radius: "))
  pi = 3.14159
  area_c = pi * (radius ** 2)
  print "\nThe circle area is  %.2f  area units" % (area_c)
  
elif shape == "T":
  base_t = float(raw_input("Enter the base of the triangle: "))
  height_t = float(raw_input("Enter the height of the triangle: "))
  area_t = (base_t * height_t) / 2
  print "\nThe triangle area is %.2f  area units" % (area_t)
  
elif shape == "R":
  base_r = float(raw_input("Enter the base of the rectangle: "))
  height_r = float(raw_input("Enter the height of the rectangle: "))
  area_r = (base_r * height_r)
  print "\nThe rectangle area is %.2f  area units" % (area_r)

else:
  print "\nThis is not a valid option"
