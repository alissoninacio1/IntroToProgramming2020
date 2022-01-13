print "\t PERSONAL BUDGET"
# PRIMEIRO VOU COLOCAR OS DADOS E DEPOIS CRIAR A TABELA

input1 = input("Enter Item 1: ")
monthy1 = float(input("Enter Item 1 Monthy Amount: "))
yearly1 = monthy1 * 12   #the yearly amount I find by multiplying the monthy amount by 12

#I'll use this, to print my data

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

input6 = input("Enter Item 6: ")
monthy6 = float(input("Enter Item 6 Monthy Amount: "))
yearly6 = monthy6 * 12 

print "\n\t\tMonthly Budget"
print "=============================================="

# now we need to write our items and values (as float)
print "\tItem       Month        Year"
print "==============================================="

print " %-10s $%-10.2f $%-10.2f" % (input1, monthy1, yearly1)foo

print " %-10s $%-10.2f $%-10.2f" % (input2, monthy2, yearly2)

print " %-10s $%-10.2f $%-10.2f" % (input3, monthy3, yearly3)

print " %-10s $%-10.2f $%-10.2f" % (input4, monthy4, yearly4)

print " %-10s $%-10.2f $%-10.2f" % (input5, monthy5, yearly5)

print " %-10s $%-10.2f $%-10.2f" % (input6, monthy6, yearly6)