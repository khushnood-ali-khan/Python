# 4 Practice Questions

# 1. write a program that print the sum of two input numbers

num = int(input("Enter First Number: "))    #we have to use type casting other wise the sum will return string output instead of sum
num1 = int(input("Enter Second Number: "))
sum = num + num1
print("Sum =",sum)

#---------------------------------------------------------------------------

# 2. Write a program that calculate the area of a square.

side = float(input("Enter One Side of the Square: "))
area = side * side        #area of a square = side * side
print("Area of the Square:",area)

#---------------------------------------------------------------------------

# 3. Write a program that print average of two floating values.

value1 = float(input("Enter First Point Value: "))
value2 = float(input("Enter Second Point Value: "))
average = (value1 + value2) / 2     #since ever calculation follows BODMAS rules so we have to close (value1 and value2) in bracket to get their sum first
print("Average of the Two Values is:",average)

#-----------------------------------------------------------------------------

# 4. Write a program that print True if input A is greater or equal to input B if not print False.

a = int(input("Enter 1st Value: "))
b = int(input("Enter 2nd Value: "))
print("A >= B =",a >= b)

#--------------------------------------------------------------------------------