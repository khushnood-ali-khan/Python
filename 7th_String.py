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
