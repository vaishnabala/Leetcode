# You have been using ast.literal_eval() to take input in a suitable format. Have you thought of how does it distinguish between different data types and data structures? We will solve a similar but smaller problem here. You will be given a string as input. You just have to determine if the string can be an integer or no?
# This is also encountered a lot in Data Science. Upon taking a lot of data, sometimes integer values are treated as a string, and due to that a lot of functionalities of integer data which you will learn ahead are rendered useless.

# ----------------------------------------------------------------------
# Input:
# A single line of string

# Output:
# INT if the input string is an integer and STR otherwise.

# ----------------------------------------------------------------------
# Sample input:
# 12

# Sample output:
# INT

# ----------------------------------------------------------------------
# Sample input:
# 12.4

# Sample output:
# STR
# Explanation: You only have to print INT if its an integer, in this case, it is a float.

#Take input using input()

# #input() takes input in form of the string
# in_string=input()
# print(in_string)
# #here extract the two numbers from the string
# ins = in_string.split(',')
# print(ins)
# x=int(ins[0])
# y=int(ins[1])

# #print x and y before swapping
# print("x before swapping: ",x)
# print("y before swapping: ",y)
# print()

# #Writing your swapping code here
# x,y = y,x

# #print x and y after swapping
# print("x before swapping: ",x)
# print("y before swapping: ",y)


