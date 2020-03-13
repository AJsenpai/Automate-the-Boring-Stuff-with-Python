# Date  : 03/12/2020
# Topic : Regular Expressions in Python
# Desc  : Extract email and phone number from a copied text from clipboard and return the extracted data to clipboard
# ######################################################################################################################################

import pyperclip, re

phoneRegex = re.compile(
    r"""(
(\d{3}|\(\d{3}\))?                 # areacode
(\s|-|\.)?                         # seprator
(\d{3})                            # first 3 digit
(\s|-|\.)                          # seprator
(\d{4})                            # last 4 digit
(\s*(ext|x|ext.)\s*(\d{2,5}))?     # extension
)""",
    re.VERBOSE,
)


# Email Regex

emailRegex = re.compile(
    r""" (  
[\w\d._%+-]+                # username
@                           # @ symbol
[\w\d.-]+                   # domain name
(\.[\w]{2,4})               # dot-something
)""",
    re.VERBOSE,
)


# find matches in clipboard
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phoneNum += " x" + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


# copy result to clipboard

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("copied to clipboard:")
    print("\n".join(matches))
else:
    print("No phone number of email address is found...")

