# Author             : Vaishnavi Balaji
# GitHub             : https://github.com/vaishnabala
# Purpose of Sharing : Learning
# Exercise           : String
# Sub Module         : A Try to Clean Coding

# Problem: Reverse the order word in a given sentence
# Condition : The letters in the word should not be reversed
# Validation : Single character/string and empty strings shouldnot be accepted

def reverse_word(inp_str):
    """Desc: This program 
       Input: String which has length more than 1
       Output: returns order reversed string """
    words = ' '                           # initialise a empty string variable called word
    for sentence in inp_str.split():      # split the given input into words
        words = sentence +'  '  + words   # reverse the order of words and save it in 'words' variable
    return words                          # return reversed words

    # Another method [You can use lines 11 to 14 instead of lines 5 to 8]
    # inp_spli = inp_str.split()
    # reversed = inp_spli[::-1]
    # words = ' '.join(reversed)
    # return words

if __name__ == "__main__":
    inp_str = input("Type a sentence to reverse the order of words:")
    if len(inp_str)>1:
        print(reverse_word(inp_str))
    else:
        print("The input should not be null")
