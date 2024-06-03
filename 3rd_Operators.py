#Operators
#-------------------------------------------------------------------------------------

#Arthimetic Operators
a=5
b=2
print("\nArthimetic Operations")
print("a + b =",a+b)      #Addition
print("a - b =",a-b)      #Subraction
print("a * b =",a*b)      #Multiplication
print("a / b =",a/b)      #Division
print("a %' b =",a%b)      #Reminder
print("a ** b =",a**b)     #Power
#--------------------------------------------------------------------------------------

#Relational Operators
print("\nRelational OR Comparison Operations")
print("a == b =",a==b)     #Equal to? ---> Output ----> False
print("a != b =",a!=b)     #Not Equal To? ---> Output ----> True
print("a > b =",a>b)      #Greater then? ---> Output ----> True
print("a < b =",a<b)      #Less Then? ---> Output ---->  False
print("a >= b =",a>=b)     #Greater or Equal? ---> Output ----> True
print("a <= b =",a<=b)     #Less or Equal? ---> Output ----> False
#--------------------------------------------------------------------------------------

#Assignment Operators
print("\nAssignment Operators")
num = 10        #num is equal to 10
print("Num :",num)
num += 5        #num which is equal to 10, is now equal to num + 5, meaning it is equal to 15 (10+5)
print("Num :",num)
num -= 5        #num which is now equal to 15 will become num - 5, meaning num will be 10 (15-5)
print("Num :",num)
num *= 2        #num which is now 10 will become num * 2, which will be equal to 20 (10*2)
print("Num :",num)
num /= 2        #num which is now 20 will become num / 2, which is 10 (20/2)
print("Num :",num)
num %= 3        #num which is 10 will become num % 2, which is 1 (10%3)
print("Num :",num)
num **= 10      #num which is 1 will remain 1 bcz 1 power 10 is 1
print("Num :",num)
#---------------------------------------------------------------------------------------

#Logical Operaters
print("\nLogical Operators")
num2 = 20
num3 = 30
print("\nNOT Operator")
print("num2(20) > num3(30) is False but with 'Not' Operator it will be:",not(num2>num3))  #originally it's False but with Not Operater it Became True
var1 = True
var2 = False
print("\nAND Operator")
print("AND Operator will return True when the two values are (True) else it will be (False), so var1 and var2:",var1 and var2)
print("(num2 < num3) and (num2 != num3):",(num2 < num3) and (num2 != num3))
print("\nOR Operators")
print("OR Operator will return True if even one value is True:",var1 or var2)
print("(num2(20)==num3(30)) or (num2 < num3):",(num2==num3) or (num2<num3))