""" List in Python: A built-in datatype that store set of values. (In other languages it's called Array). 
                    But it can store elements of different types (integers,floats,string etc).
"""
#Example:
marks = ["1st Semester Marks",72,64,85,84,81,88]

print("\nMarks Lists:",marks)             #Output ---> Marks Lists: [72,64,85,84,81,88]
print("Marks Datatype:",type(marks))    #Output ---> Marks Datatype: <class 'list'>
print("Length of List:",len(marks))     #Output ---> Length of List: 7

#to access a spacific value you can do it by mentioning it's index number, Example:
print("Value 3 is:",marks[2])           #Output  ---> Value 3 is: 85   OR
print("Value 1 is:",marks[0])           #Output ----> Value 1 is: 1st Semester Marks

#NOTE list are muteble unlike string that are immutable (mean we can't change its value), Example:
marks[0] = "Khushnood"
print("Value 1 is Now:",marks[0])       #Output ---> Value 1 is Now: Khushnood
#----------------------------------------------------------------------------------------

#List Slicing:  Syntex:-> list_name[starting_index : ending_index]

paper_marks = [88,85,84,81,72,64]
print("\nSlicing:",paper_marks[0:4])  #Output --> Slicing: [88, 85, 84, 81]    #ending index won't be included.
"""
#Extra Consepts: 
1). paper_marks[ :4]    #python auto understance to start from zero.    #Ouput --> [88, 85, 84, 81]
2). paper_marks[0:len(paper_marks)]     #it mean from zero to end index. #Output --> [88,85,84,81,72,64]
3). paper_marks[0: ]    #auto understance that from zero to end     #Output --> [88,85,84,81,72,64]
# 4). Negative index: 
paper_marks[-6:0]  #you can also count from back side in negative numbers. #Ouput -->  [88,85,84,81,72,64]
"""
#------------------------------------------------------------------------------------------

#List Method: Different Functions that can be only use for lists. #Example:

list = [2, 1, 3]

list.append(4)  #Add the element to the end of list. 
print("\nAdd 4 to list:",list)     #Output ----> [2, 1, 3, 4]

list.sort()     #sort the list elements in ascending order. 
print("Sorted in Ascending order:",list)     #Output ----> [1, 2, 3, 4]

list.sort(reverse=True)     #sort the list elements in Decending order.
print("Sorted in Decending order:",list)                 #Output ----> [4, 3, 2, 1]

list.reverse()      #reverse the list elements.
print("Reverse the elements:",list)         #Output ----> [1, 2, 3, 4]

list.insert(2,2.5)  #insert element on specific index.
print("Insert 2.5 on 2 index:",list)         #Output ---> [1, 2, 2.5, 3, 4]

list.remove(2.5)    #remove the first occurence of the element.
print("Remove the first occur of 2.5:",list)         #Output ---> [1, 2, 3, 4]  #it remove the first occurence of 2.5.

list.pop(3)         #remove the element from specific index.
print("Remove the 3 index(4):",list)         #output ---> [1, 2, 3]