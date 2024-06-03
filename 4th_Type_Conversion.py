#Type Conversion:-> To convert the type of variable to another type.
#Two Types Of Conversion.

#1. Implicit Conversion:->
#In Implicit Conversion Interpreter Automatically change the Datatype of variable.
print("Implicit Conversion:")
a = 3       #int datatype
b = 4.5     #float datatype
print("Datatype of a:",type(a))
print("Datatype of b: ",type(b))
sum = a + b     #since a is int and b is float type and float is superior (mean it contain more space compare to int),---> 
                #---> so the interpreter will automatically change a (which is int type) into float type.
print("Sum of a + b:",sum)      #output ---> 3 + 4.5 --> 7.5
#----------------------------------------------------------------------------

#2. Explicit Conversion or Typecasting:->
#In TypeCasting we have to change the Type of a variable Manually.
print("\nCasting type:") # \n is use to break line and jump to new line.
c = "3"         #string datatype
d = 5.5         #float datatype
print("Datatype of c:",type(c))
print("Datatype of d:",type(d))
#since float type and string type can't be added we have to change string value to int or float type.
c = int(c)          #To change it to int we have to use int function int(variable).
print("Now the Datatype of c is:",type(c))
add = c + d     #Now the value of c is an int type.
print("Sum of c + d:",add)      #output 3 + 5.5 ----> 7.5
#---------------------------------------------------------------------------------
#NOTE Character type data can't be changed into int or float example "Khushnood" it cann't be cahnge to int or float type.