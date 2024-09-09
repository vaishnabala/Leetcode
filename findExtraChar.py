# Author             : Vaishnavi Balaji
# GitHub             : https://github.com/vaishnabala
# Purpose of Sharing : Learning
# Exercise           : String
# Sub Module         : A Try to Clean Coding

# Given two strings, one of the strings will contain an extra character. Find the extra character. 
# The number of all the other characters in both the strings will be the same.
# The code will be case sensitive.
# Input: Two strings on two separate lines. 
# Output: One Character which is extra in one of the strings
# Sample input:
# abcd
# cedab
# Sample output:
# e

import re

input_str1 =  input("Enter First String : ")
input_str2 =  input("Enter Second String : ")

if (len(input_str1)>len(input_str2)):
    x,y = input_str1,input_str2
    print(x,y)
elif(len(input_str1)<len(input_str2)):
    x,y = input_str2,input_str1
    print(x,y)
else:
    print("Input Error")

for letters in range(len(x)-1):
    if x.count(x[letters]) != y.count(y[letters]):
        print(x[letters])
        # if x[letters] not in y:
        #     print(x[letters])
