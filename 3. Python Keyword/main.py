# # Python code to demonstrate working of iskeyword()

# # importing "keyword" for keyword operations
# import keyword

# # printing all keywords at once using "kwlist()"
# print("The list of keywords is : ")
# print(keyword.kwlist)
#--------------------------------------

# print(False == 0)
# print(True == 1)

# print(True + True + True)
# print(True + False + False)

# print(None == 0)
# print(None == [])
#-------------------------------------

# # showing logical operation
# # or (return True)
# print(True or False)

# #showing logical operation
# # and (returns False)
# print(False and True)

# # showing logical operation
# # not (returns false)
# print(not True)

# # showing logical operation
# # not (returns False)
# print(not True)

# # using "in" to check
# if 's' in 'geeksforgeeks':
#     print("s is part of geeksforgeeks")
# else:
#     print("s is not part of geeksforgeeks")

# # using "in" to loop through
# for i in 'geekforgeeks':
#     print(i, end=" ")

# print("\r")

# # using is to check object identity
# # string is immutable( cannot be changed once allocated)
# # hence occupy different memory location
# print(' ' is ' ')

# # using is to check object identity
# # string is immutable( can be changed once allocated)
# # hence occupy different memory location
# print({} is {})
#----------------------------------------------------

# # Using for loop
# for i in range(10):

#     print(i, end = " ")

#     # break the loop as soon it sees 6
#     if i == 6:
#         break

# print()

# # loop from 1 to 10
# i = 0

# while i <10:

#     # if i is equals to 6,
#     # continue to next iteration
#     # without printing
#     if i == 6:
#         i+= 1
#         continue
#     else:
#         # otherwise print the value
#         # of i
#         print(i, end = " ")

#     i += 1
#-------------------------------------------

# Python program to illustrate if-elif-else ladder
#!/usr/bin/python

# i = 20
# if (i ==10):
#     print ("i is 10")
# elif (i == 20):
#     print ("i is 20")
# else:
#     print ("i is not present")

#--------------------------------------

# # fed keyword
# def fun():
#     print("Inside Function")

# fun()
#---------------------------------------

# # Return keyword
# def fun():
#     S = 0

#     for i in range(10):
#         S += i
#     return S

# print(fun())

# # Yield Keyword
# def fun():
#     S = 0

#     for i in range(10):
#         S += i
#         yield S

# for i in fun():
#     print(i)
#---------------------------------

# Python3 program to
# demonstrate instanting
# a class


# class Dog:

#     # A simple class
#     # attribute
#     attr1 = "mammal"
#     attr2 = "dog"

#     # A sample method
#     def fun(self):
#         print("I'm a", self.attr1)
#         print("I'm a", self.attr2)

# # Driver code
# # Object instantiation
# Rodger = Dog()

# #Accessing class attributes
# # and method through objects
# print(Rodger.attr1)
# Rodger.fun()
#--------------------------------------

# # using with statement
# with open('file_path', 'w') as file:
#     file.write('hello world !')
#---------------------------------------

# import math as gfg

# print(gfg.factorial(5))
#---------------------------

# n = 10
# for i in range(n):

# # pass can be used as placeholder
# # when code is to added later
#     pass
#-----------------------------------

# # Lambda keyword
# g = lambda x: x*x*x

# print(g(7))
#-------------------------------

# # import keyword
# import math
# print(math.factorial(10))

# # from keyword
# from math import factorial
# print(factorial(10))
#--------------------------------

