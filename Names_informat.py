# Author             : Vaishnavi Balaji
# GitHub             : https://github.com/vaishnabala
# Purpose of Sharing : Learning
# Exercise           : String
# Sub Module         : A Try to Clean Coding
# Problem            : 
#     You will be given a string, containing a few spaces and random upper and lower cases. 
#     You have to write a code that will add underscore in place of spaces and also capitalise the letters properly, 
#     i.e. the first letter after underscore should be in upper case and the first letter of the string should be in upper case, all of the other letters should be lower case. 
# Input: data science
# Output: Data_Science 
# Validation : 
#   1. The input must be string. No special Char and symbols
#   2. Spaces allowed between two string/char but no empty string
#   3. Input should have More than 2 characters
#   4. Single word is allowed



import re                # import to use regex

def titleCase(inp_str):   
    """ Desc: Changes first letter to upper and rest to lower case and replaces spaces with underscore
        Input: valid string(words or names)
        Output: Title cased with underscore text - string"""
    inp_spl = inp_str.split()                        #splits the word and stores as list 
    format_word = [word[0].upper() + word[1:].lower() for word in inp_spl] # iterates over list to change the first letter to upper remaining lower
    format_word= '_'.join(format_word)       # Join the words in the list with underscore delimiter
    return format_word                       # return the formatted list

def validstr(inp_str):
    """Desc: Validates the input string if it has only string
       Input: input string
       Output: bool: if passes string is valid, retrun true otherwise false"""
    inp_str = inp_str.strip()                    # removes extra space from start and end position of the string
    if (not inp_str)  or ('  ' in inp_str):      # checks if input is not empty string and doesnt have more spaces in between
        return False
    if re.match(r'^[A-Za-z]+( [A-Za-z]+)*$', inp_str) :  # Checks if the input has only letters and spaces
        return True                          # returns true if it does
    else:
        return False                         # returns false otherwise

if __name__ == "__main__":
    inp_str = input("Enter the string:")       # input from user
    if validstr(inp_str) is True and (inp_str!='') is True and len(inp_str)>2:        # checking if the input is valid,not null and has more than two characters
        print(titleCase(inp_str))              #Call the titlecase func passing input parameter
    else:
        print("\nEnter a valid string. \nNote:It should have more than one letter. \
              \n\tOnly alphabets and spaces are allowed. \
              \n\tMultiple Spaces are not allowed") # User message- guides/tells user to give valid input

