# Problem: You will be given two strings. You have to find the largest prefix common in both the strings.
# Input:  Two lines of input, one string on each line
# Output: The common largest prefix for both strings. Check sample input/output for clarification. -1 if no prefix is common.
# Sample input:
# String Input 1 = 'abshdksajd'
# String Input 2 = 'abshiehand'
# Sample output: = absh
import re                                      # import to use regexp

def commonPrefix(inp_str1,inp_str2):
    """ Desc: Identify common prefix in given strings and print
        Input: Two string values
        Output: Returns integer i - index , if no match return -1"""
    inp_str1 = inp_str1.lower()
    inp_str2 = inp_str2.lower()
    slen = min(len(inp_str1),len(inp_str2))
    if inp_str1 == inp_str2:
        return len(inp_str1)
    
    for i in range(slen):
        if inp_str1[i] != inp_str2[i]:
            break
    if i == 0:
        return -1
    else:
        return i

def validchk(inp_str1,inp_str2):
    for i in [inp_str1,inp_str2]:
        if re.match(r'^[a-zA-Z\s]+$',i):
            pass
        else:
             return False
    return True
    
    
inp_str1 = input("Enter String 1 : ")
inp_str2 = input("Enter String 2 : ")

if validchk(inp_str1,inp_str2) is True and inp_str1!= ' ' and inp_str2!= ' ':
    i = commonPrefix(inp_str1, inp_str2)
    if i<0:
        print("No Match")
    else:
        print(inp_str1[:i])
else:
    print("Invalid Input")
    




inp_str1=input()
inp_str2=input()
inp_str1 = inp_str1.lower()
inp_str2 = inp_str2.lower()
slen = min(len(inp_str1),len(inp_str2))
for i in range(slen):
    if inp_str1[i] != inp_str2[i]:
        break
if i == 0:
    print("-1")
else:
    print(inp_str1[:i])