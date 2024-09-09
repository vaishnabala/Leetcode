# Author             : Vaishnavi Balaji
# GitHub             : https://github.com/vaishnabala
# Purpose of Sharing : Learning
# Exercise           : String
# Sub Module         : A Try to Clean Coding
# Problem            : 
#   Two strings are anagrams of each other if you can rearrange the characters of one string to make the other string.
#   Given two strings, can you find if they are anagrams or no?
# Input: night,thing
# Output: True 
# Validation : 
#   1. The input must be string. No special Char and symbols
#   2. Spaces allowed between two string/char but no empty string and no multiple space
#   3. Atleast one of the two- Input should have More than 2 characters
#   4. Single word is allowed


import re                 # import to use regexp

def anagram(inp_str1,inp_str2):
    """Desc: Checks if the letters of one string is present in another string
       Input :  Two parameters, both are strings
       Output: Returns bool, True or False"""
    inp_str1 = inp_str1.lower()               # Convert string to lower
    inp_str2 = inp_str2.lower()               # Convert string to lower
    if len(inp_str1)!=len(inp_str2):          # checks if the lengths are equal to prove anagram
        return False                           # returns false if len is not equal
    else:
        # for letters in inp_str1:               # splits the letter in string
            # if letters not in inp_str2:        # checks if a char/Letter in one string is  not in another
            #     return False                   # return false as result because if letter is not present in another string 
            # else:
            #     return True
        for i in range(len(inp_str1)):        # Iterate through lenght
            if inp_str1.count(inp_str1[i]) != inp_str2.count(inp_str2[i]):   # check the count of each letter if they are equal
                return False                                                 # return false if the count of each letter is not equal
            else:        
                return True                                                  # returns true if the count is equal
        

def validchk(inp_str1,inp_str2):
    """ Desc: Validates the given input string 
        Input: Two string
        Output: Bool- True or False, If string is valid, it will retun true otherwise false"""
    for i in [inp_str1,inp_str2]:                       # Given strings are accessed iteratively in a for loop
        if (not i) or ('  ' in i):                      # checks if the string is not empty, not doesnt contain multiple space
            return False                                # return false if both conditions false 
        if re.match(r'^[a-zA-Z]+( [a-zA-Z]+)*$',i):     # check the if the string has only alphabets- a to z,A to Z and space for more than one word
            return True                                 # returns true if the pattern matches
        else:
            return False                                # returns false if pattern fails
        
if __name__ == "__main__":
    inp_str1 = input("Enter String 1 : ")               # Get String 1 from user
    inp_str2 = input("Enter String 2 : ")               # Get String 1 from user
    if validchk(inp_str1,inp_str2) is True:             # call the validation function, and  checks if its true
        print(anagram(inp_str1,inp_str2))               # print the output of anagram function
    else:
        print("\nEnter a valid string. \nNote:It should have more than one letter. \
              \n\tOnly alphabets and spaces are allowed. \
              \n\tMultiple Spaces are not allowed")      # helps user to give proper input, executed when the input is invalid
