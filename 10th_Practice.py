#Practice on Conditional Statements

#1). Write a program to Grade students base on their Marks.
marks = float(input("Enter Your Marks: "))
if (marks >= 90):
    print("Your Grade is A.")
elif (marks >= 80):
    print("Your Grade is B.")
elif (marks >= 70):
    print("You have C Grade.")
elif (marks >= 60):
    print("You have D Grade.")
else:
    print("You are Fail.")
#---------------------------------------------------------------

#2). WAP to check if the number enter by user is even or odd.
num = int(input("Enter a Number: "))
if (num % 2 == 0):
    print("The Number is Even.")
else:
    print("The Number is Odd.")
#-----------------------------------------------------------------

#3). WAP to find the greatest of the 3 numbers enter by user.
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
if (num1 == num2 and num2 == num3):
    print("They are all same.")
elif (num1 >= num2 and num1 >= num3):
    print(num1," is greater.")
elif (num2 >= num1 and num2 >= num3):
    print(num2," is greater.")
else:
    print(num3," is greater.")
#-----------------------------------------------------------------

#4). WAP to find if the number is multiple of 7 or not.
num4 = int(input("Enter a Number: "))
if (num4 % 7 == 0):
    print(num4,"is multiple of 7.")
else:
    print(num4,"is not multiple of 7.")