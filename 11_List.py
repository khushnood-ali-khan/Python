""" List in Python: A built-in datatype that store set of values. (In other languages it's called Array). 
                    But it can store elements of different types (integers,floats,string etc).
"""
#Example:
marks = ["1st Semester Marks",72,64,85,84,81,88]

print("Marks Lists:",marks)             #Output ---> Marks Lists: [72,64,85,84,81,88]
print("Marks Datatype:",type(marks))    #Output ---> Marks Datatype: <class 'list'>
print("Length of List:",len(marks))     #Output ---> Length of List: 6

#to access a spacific value you can do it by mentioning it's index number, Example:
print("Value 3 is:",marks[2])           #Output  ---> Value 3 is: 85   OR
print("Value 1 is:",marks[0])           #Output ----> Value 1 is: 1st Semester Marks

#NOTE list are muteble unlike string that are immutable (mean we can't change its value), Example:
marks[0] = "Khushnood"
print("Value 1 is Now:",marks[0])       #Output ---> Value 1 is Now: Khushnood
