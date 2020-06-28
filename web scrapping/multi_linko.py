import webbrowser, pyperclip

links = pyperclip.paste().split()
# print(links)
for link in links:
    webbrowser.open_new_tab(link)

