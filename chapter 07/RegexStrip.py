# Date : 03/12/2020
# Topic : Regular Expressions
# Description : Regex version of strip method in python
#
# ### Practice Project ###
# Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than
# the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters 
# specified in the second argument to the function will be removed from the string
# #######################################################################################################################################

import re 

def stripfunc(text,remove):
    if remove == '':
        stripRegex = re.compile(r'^\s*')
        new_string = stripRegex.sub('',text)
        stripRegex = re.compile(r'\s*$')
        new_string = stripRegex.sub('',new_string)
        return new_string
    else:
        stripRegex = re.compile(remove)
        new_string = stripRegex.sub('',text)
        return new_string


mytext = input("Enter a text to perform strip\n")
strip_action = input("which character do you want to remove from text? [default= space]\n")

print(stripfunc(mytext,strip_action))
