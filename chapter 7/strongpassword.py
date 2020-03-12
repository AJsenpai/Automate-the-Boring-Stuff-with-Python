# Date: 03/05/2020
# Topic : Regular Expression with Python
#
### Practice Project ###
# Strong Password Detection
# Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as 
# one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to 
# test the string against multiple regex patterns to validate its strength.
# ######################################################################################################################################


import re,getpass

def password_checker(pwd_to_check):
    # you can also use re.match(r'regualar expression') with if to check the Regex 
    uppercheck = re.compile(r'[A-Z]')
    lowercheck = re.compile(r'[a-z]')
    digitcheck = re.compile(r'[0-9]')
    specialchar = re.compile(r'[@#$%^&*+=]')
    
    moupper = uppercheck.search(pwd_to_check)
    molower = lowercheck.search(pwd_to_check)
    modigit = digitcheck.search(pwd_to_check)
    mospecial = specialchar.search(pwd_to_check)
    
    # passwordRegex = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')
    # if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', pwd_to_check):
    if len(pwd_to_check)>7 and mospecial and modigit and molower and moupper:
        print("your password is Strong")
    else:
        print(""" \nPassword Rules:
                  * Password should have min length of 8 characters
                  * Atleast one uppercase letter
                  * Atleast one lowercase letter
                  * Atleast one digit
                  * Atleast one special Character = @#$%^&*=+
                  """)
        
# password = input("Enter your password  ")
password = getpass.getpass("Enter you password ")
seepassword= input ("press any key to see your paasword else press Enter?\U0001F441   ")

if seepassword == "":
    password_checker(password)
else:
    print(password)
    password_checker(password)

