# Date: 03/06/2020
# Topic : Regular Expression
# Description : Regular expression to validate Email Address and Mobile Number
# #########################################################################################################################################

import re
def emailphone_check(email,phone):
    
#     emailregex= re.match(r'^([\w\d]+)@([\w\d]+)\.([\w\d]{2,3}$)',email)  # use of + instead of {} 
    emailregex= re.match(r'^([\w\d]{1,})@([\w\d]{2,})\.([\w\d]{2,3}$)',email)
    phoneregex= re.match(r'^\+(\d){2,4}-(\d){5}-(\d){5}$',phone)
    
    print("valid email") if emailregex else print("invalid email")
    
    print("Valid phone number") if phoneregex else print("invalid phone number")
    
emailphone_check("infhgy@gma23.co",'+91-34567-87654')

