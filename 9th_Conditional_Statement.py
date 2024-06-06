#Conditional Statements: Use to check certain condition.
"""
Syntex: 
if (Condition):
    Statement 1

elif (Condition):                       (else if) full form
    Statement 2

else:
    Statement N
"""
#Example: 
age = 10
if ( age >= 18):     #if the condition is True it will execute the statement else it will jump to next condition.
    print("You are an Adult.")  #Before we write a statement we must give 4 spaces or one tab space (indentation).

else:   #if the first condition wasn't True it will execute this statement.
    print("You are a kid.")
#------------------------------------------------------------------------------------
#if you have more then two conditions you can use elif (else if) too. Example:
"""
Write a program that takes an integer as input and checks if it is positive, negative, or zero. 
If the number is positive, print “The number is positive.” If the number is negative, 
print “The number is negative.” Otherwise, print “The number is zero.” 
"""
num = int(input("Enter a Number: "))
if (num > 0):
    print("The Number is Positive.")

elif (num == 0):
    print("The Number is Zero.")

else:
    print("The Number is Negative.")