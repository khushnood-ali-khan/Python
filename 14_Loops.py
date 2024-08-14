# #Loops :-> Loops are used to repeat instructions.
# #Two Types :-> While Loop and For Loop.
# """ 
# 1). While Loop :-> It execute the block of code as long as the given condition become true.
#     Syntex :->
#             while condition :
#                     # block of code
# Example:

# while True:
#     print("Hello World!")           #Output --> Hello World!    (infinite time)
# """

# i = 1
# while i <= 5 :
#     print("Hello World!")              #Output --> Hello World!     (print 5 times)
#     i += 1 

# #------------------------------------------------------------------------------------------------
# # Practice Questions :
# # 1). Print numbers form 1 to 100.

# num = 1
# while num <= 100:
#     print(num)
#     num += 1

# # 2). Print numbers from 100 to 1.

# num2 = 100
# while num2 >= 1:
#     print(num2)
#     num2 -= 1

# # 3). Print the multiplication table of number n.

# n = int(input("Enter a Number: "))
# j = 1
# while j <= 10:
#     print(n,"*",j,"=",n*j)
#     j += 1

# # 4). Print the element of the following list using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].

# Lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# k = 0
# # cnt = print(len(Lst))
# while k <= len(Lst)-1:
#     print(Lst[k])
#     k += 1

# 5). Search for a number x in this tuple using loop: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100).

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a number: "))
l = 0
while l <= len(tup)-1:
    if x == tup[l]:
        print("The number is in List.")
        break
    else:
        print("The number isn't in list.")
    l += 1