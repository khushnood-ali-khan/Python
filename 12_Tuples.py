# Tuples:- A built-in datatype that lets us create immutable (not changable) sequence of values.
# Data in Tuples can't be changed unlike List where we can change it's data.

marks = (10, 30, 40, 50)
print(type(marks))
print("The Fourth value is: ",marks[3])      #Output ---> <class 'tuple'>    The Fourth value is:  50


# In tuple if we have single digit value we most put , in the end.  Example

value = (1,)
print(type(value), value)       #Output --->    <class 'tuple'> (1,)

# Slicing:-

tup = (1, 2, 3, 4, 5)
print(tup[0 : 3])               #Output --->    (1, 2, 3)