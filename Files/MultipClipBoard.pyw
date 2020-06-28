# The .pyw extension means that Python won’t show a Terminal window when it runs this program.
"""
mcb.pyw - Saves and loads pieces of text to the clipboard.
Usage:  py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
        py.exe mcb.pyw list - Loads all keywords to clipboard.
"""
import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")

# save clipboad content
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    # list keywords and load content
    if sys.argv[1].lower() == "list":
        # string representation of keys will be copied to clipboard
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
# print(list(mcbShelf.keys()), list(mcbShelf.values()))


mcbShelf.close()
