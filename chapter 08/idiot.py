# Date: 03/13/2020
# Topic : input validation using pyinputplus module
# Desc: practice program to check check for input validation yes or no
# #########################################################################################################################################

import pyinputplus as pyip 
while True:
  prompt = "Want To Know how to keep the Idiot busy for hours? \n"

  response = pyip.inputYesNo(prompt)  # will validate case insensitive value as well including Y/y N/n
  if response=="no":
    break
print("Thank You have a nice day")
