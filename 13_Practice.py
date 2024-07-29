# Practice Questions on List and Tuples.

# 1). Write a program to ask the user to enter names of their 3 favorite movies and store it in list.

print("Enter the names of your 3 favorite movies")
movie = input("1st: ")
movie1 = input("2nd: ")
movie2 = input("3rd: ")
movies = [movie, movie1, movie2]
print(movies)

# OR

Movies = []
Movies.append(input("Enter Your 1st Favorite Movie: ")) 
Movies.append(input("Enter Your 2nd Favorite Movie: ")) 
Movies.append(input("Enter Your 3rd Favorite Movie: ")) 
print(Movies)

#-------------------------------------------------------------------------------------------------------

# 2). WAP to check if a list contain palindrome of elements. {1, 2, 3, 2, 1}

list = [1, 2, 3, 2, 1]
palindrome = list.copy()
list.reverse()
print(list)
if (list == palindrome ):
    print("The List is Palindrome.")

else:
    print("List isn't Palindrome.")
  
#---------------------------------------------------------------------------------------------------------

# 3). WAP to count the number of students with grade "A" in the following tuple.
#  ["C", "D", "A", "A", "B", "B", "A"]

tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))
