#Input in python

print("Enter somthing:")
input()     #take input from the keyboard

#OR
input("Enter somthing: ")    #we can also print output on the screen with input() function.
#it will print the "string" on the screen and also will accept input from keyboard.
#the input it accept will be string type by default even if its digital value.

#Example
name = input("Enter Your Name: ")
age = input("Enter Your Age: ")
print("Name You Entered:",name,". It's type:",type(name))
print("Age You Entered:",age,". It's type:",type(age))
#Both Name and Age will be <str> string type.
#-------------------------------------------------------------------------------

#if we want a specific type of data we have to mention its type. 
#Example we want int type of data so we will use typecasting.
num = int(input("Enter a number: "))
print("You Entered:",num,"Its Type is:",type(num))
#Another Example
num2 = float(input("Enter a Point Value: "))
print("You Entered:",num2,"Its Type is:",type(num2))
#------------------------------------------------------------------------------------

#Write a Program That take student information.
student_name = input("Enter Your Name: ")         #it will accept string value.
student_age = int(input("Enter Your Age: "))      #it will be integer value.
student_gpa = float(input("Enter Your Gpa: "))    #it will be float value.
print("Your Name is:",student_name)
print("Your Age is:",student_age)
print("Your Gpa is:",student_gpa)