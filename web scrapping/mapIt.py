# mapIt.py
# launches a map into browser using an address from the command line arguments or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # get the address from command line
    address = "".join(sys.argv[1:])
else:
    # get the address from clipboard
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
