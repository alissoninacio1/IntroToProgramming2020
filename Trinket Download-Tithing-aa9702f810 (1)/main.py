
#INPUT ARE FIRST

moneyEarned = float(input("\nEnter How much money you earned this month, please: "))
yearEarned = moneyEarned * 12

t_a= "Tithing" # only to use as a reference
tithing_ = moneyEarned * 0.10   # Tithing Owed = 10% of moneyEarned
t_year = tithing_ * 12



f_a = "FastOff" #only tu use as a reference
fastOffering = float(input("\nEnter how much you would like to pay for fast offerings, please: "))
f_year = fastOffering * 12 

#here is the last week code

input1 = input("Enter Item 1: ")
monthy1 = float(input("Enter Item 1 Monthy Amount: "))
yearly1 = monthy1 * 12

input2 = input("Enter Item 2: ")
monthy2 = float(input("Enter Item 2 Monthy Amount: "))
yearly2 = monthy2 * 12 

input3 = input("Enter Item 3: ")
monthy3 = float(input("Enter Item 3 Monthy Amount: "))
yearly3 = monthy3 * 12 

input4 = input("Enter Item 4: ")
monthy4 = float(input("Enter Item 4 Monthy Amount: "))
yearly4 = monthy4 * 12 

input5 = input("Enter Item 5: ")
monthy5 = float(input("Enter Item 5 Monthy Amount: "))
yearly5 = monthy5 * 12

#Following, I wrote the variables for the last  information

m_total = moneyEarned - (monthy1 + monthy2 + monthy3 + monthy4 + monthy5)

y_total = yearEarned - (yearly1 + yearly2 + yearly3 + yearly4 + yearly5)

#here I'll print the complete budget
print "\nPersonal Budget"
print "==" * 25

print "Expenses    Month      Year"
print "==" * 25

print  "\t    $%-10.2f $%-10.2f" % (moneyEarned, yearEarned)

print "==" * 25 

#the last week code names

print "Expenses    Month      Year"
print "==" * 25

print " %-10s $%-10.2f $%-10.2f" % (t_a, tithing_, t_year)
print " %-10s $%-10.2f $%-10.2f" % (f_a, fastOffering, f_year)

print " %-10s $%-10.2f $%-10.2f" % (input1, monthy1, yearly1)

print " %-10s $%-10.2f $%-10.2f" % (input2, monthy2, yearly2)

print " %-10s $%-10.2f $%-10.2f" % (input3, monthy3, yearly3)

print " %-10s $%-10.2f $%-10.2f" % (input4, monthy4, yearly4)

print " %-10s $%-10.2f $%-10.2f" % (input5, monthy5, yearly5)

print "==" * 25
print "Savings     Month      Year"
print "==" * 25

print  "\t    $%-10.2f $%-10.2f" % (m_total, y_total)
