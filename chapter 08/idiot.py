# Date: 03/13/2020
# Topic : input validation using pyinputplus module
# #########################################################################################################################################

import pyinputplus as pyip 
while True:
  prompt = "Want To Know how to keep the Idiot busy for hours? \n"

  response = pyip.inputYesNo(prompt)
  if response=="no":
    break
print("Thank You have a nice day")
