import re                              # import to use regexp
def movVowel(inp_str):                 # module to move vowel one side and others otherside
    """Desc: Module to move vowels in a given string at the start and others toward the last
       Input: String input- May be a word or sentence
       Output: returns concatenated (Vowels and consonents)string"""
    vow = ''                             # declare vow variable to store vowel in a given string
    others = ''                          # declare others variable to store non vowels in a given string
    for words in inp_str:                # iterats through all characters in input string
        if words in ['aeiouAEIOU']:         # checks if the each character is a vowel
            vow = vow+words                                            # concatenates with vow variable if character is vowel
        else:                           
            others = others+words                                      # concatenates with others variabel if character is non vowel    
    return (vow+others)                                                # concatenate vow and others and return

def validchk(inp_str):  
    """Desc: Validates the input string if it has only string
       Input: input string
       Output: bool: if passes string is valid, retrun true otherwise false"""                                               
    if re.match(r'^[a-zA-Z\s]+$',inp_str):    # checks if the inp_str has only a-z ,A-Z and space character
        return True                           # returns True if it is only allowed string
    else:
        return False                          # returns False if it doesnot have valid one

if __name__ == "__main__":
    inp_str = input("Enter a string  :")            # get the input from user
    if inp_str!=' ' and validchk(inp_str) is True:  # checks if the string is empty and calls validchk function and allows if returns true
       print(movVowel(inp_str))                     # calls movVowel module with inp_str parameter
    else:
        print("Enter a valid string")               # prints user message if the string is empty and if validchk returns false
