# Author             : Vaishnavi Balaji
# GitHub             : https://github.com/vaishnabala
# Purpose            : Learning
# Exercise           : String
# Sub Module         : Clean Coding


# Problem: Check if the given string in Palindrome
# Conditions: 
#      1. Only string are accepted - No special characters, no numbers
#      2. Single String is not considered as Palindrome
#      3. Input is only word not a sentence
#      4. Two logics are presented


import re                            # import to use Regular expressions
def palindrome(inp_str):
    '''Desc: To convert the valid string to palindrome
       Input: String to be checked
       Output: Print if the given string is palindrome or not'''
    
    inp_str = inp_str.lower()                  # convert the string to lower case facilitates it to compare
    if inp_str == inp_str[::-1]:               # checking if the reverse is equivalent to original
        return True                            # Return true if condition passes
    else:
        return False                           # Return false if condition fails
    
    #Another Logic  [you can use lines 28 to 34 (or) 22 to 25]:
    # r=''                      # initialise string called r - to save reversed string
    # for i in inp_str:         # loop to seperate the characters  string
    #      r = i+r              # insert characters in reverse order, insertion will insert char at index [0] here
    # if r == inp_str:          # checking if the reverse is equivalent to original
    #     return print("Yes its Palindrome")     # Print yes if its palindrome
    # else:
    #     return print("No it's not a Palindrome")    # Print no if its not
    

def validstr(inp_str):
    ''' Desc : Check if the input string is valid sting(allows only a - z and A-Z)- no space/special chars
        Input: string - a word
        output: returns true if its a valid string(allows only a-z and A-Z)- no space/special chars otherwise false'''
    if re.match(r'^[a-zA-Z]+$',inp_str) and len(inp_str)>1:      # checking if it's valid(only a-z and A-Z)- no space/special chars 
            return True                       # Returns true if its valid
    else:
            return False                      # Returns true if its valid

if __name__ == "__main__":
    inp_str = input("This is Program for checking if the string is palindrome\
                    Enter the string to be checked:")  # get the input from user
    if validstr(inp_str) is True:                       # call checkstr and check if its valid string
        if palindrome(inp_str) == True:
            print("Yes its Palindrome")         # Print yes if its palindrome           
        else:
            print("No it's not a Palindrome")   # Print no if its not                    # call palindrome function if its true
    else:
        print("Please enter Valid String input")         # otherwise tell the user to give valid input
