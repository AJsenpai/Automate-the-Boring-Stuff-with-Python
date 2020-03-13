#! python3
# Date: 03/01/2020
# Topic : Manipulating Strings
# Description: add wikipedia bullet point to the start of each line of text on the clipboard
# ########################################################################################################################################
import pyperclip

text = pyperclip.paste()
pyperclip.copy(text)

# seprate lines and add stars

lines = text.split("\n")
while "\r" in lines:  # remove empty lines from the clipboard
    lines.remove("\r")


for i in range(len(lines)):  # loop through all the indexes in the list
    if not lines[i].startswith("*"):
        lines[i] = "* " + lines[i]

text = "\n".join(lines)

pyperclip.copy(text.strip("\n"))

