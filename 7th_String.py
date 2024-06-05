 #String :-> String is a datatype that stored sequence of characters.
example = "Hello World!"    #string can be written in single, Double or Triple Quotes (".....",'....',""".....""").

#Concatenation :-> the process of adding two strings.
#Example:
str1 = "Hello"
str2 = "World"
add = str1 + str2
print("Concatenation:->",add)          #output ---> HelloWorld

#And if you want to put a space in their you can do it like this.
space = str1 + " " + str2       #you can add space in it like this it valid in Python.
print("Now a Space in it :->",space)        #Output ---> Hello World

#Length of the string :-> A builten function used to find length of the string.
#Example:
print("Length of the String is:->",len(space))     #Output ---> Length of the String is: 11
#--------------------------------------------------------------------------------------

#Indexing :-> In String every Character is assign to special position which start from zero to in so on.....
#Example:
indexing = "Hello World"
print(indexing[0],"Is On Position Zero.")      #Output ---> H Is On Position Zero.

#NOTE We can't change the character with indexing. Example:
"""
name[1] = "o"    # I want name[1] which is e to replace it with o, so that is incorrect and it will give us an error.
print(name)
"""
#-----------------------------------------------------------------------------------------

#Slicing :-> Slicing a string and accessing different parts of it.
#Syntex :-> name_of_string[starting_index : ending_index]       #ending index won't be included. Example:

name = "Khushnood"
print("Slicing name 'Khushnood' :->",name[0:5])    #Output ---> Slicing name 'Khushnood' :-> Khush  n won't be included
#Extra concepts:-> 1). name[0:] --> if i miss to add ending index then python will automatically understand that i -->
                                     #--> want to go to the last word so Output will be:-> Khushnood
                # 2). name[0:len(str)]  --> it also mean that i want to go to the last word. output --> Khushnood
                # 3). name[:5] --> if we miss the first index then python will automatically start from zero. output--> Khush

#Negative indexing:-> In negitive slicing we can cout from backword, which start from -1.
#Example:
print("Negative Slicing:-> ",name[-9:-4]) #output ---> Khush
#--------------------------------------------------------------------------------------------

#String Functions:
#Example:
string = "hi I am Khushnood Ali Khan"

print(string.endswith("an"))   #with this function i want to check if my string ends with 'an' if it does then it will --->
                               #---> return True or else it will return False. Output --> True

print(string.capitalize())   #This function will Capitalize the first word of the string. Output--> Hi I am Khushnood Ali Khan
                             #It won't change the value, only a copy of it will be changed. example if i access the string -->
                             #elsewhere it will be the same is original 'hi I am khushnood Ali Khan'.

print(string.replace("u","o")) #use the to replace character or word in a string.

print("am is first occur on index:->",string.find("am"))    #returns the first index of first occurrer. Output --> 5

print("a occur in a string:->",string.count("a"))   #Use to count or check the number of occurrences.