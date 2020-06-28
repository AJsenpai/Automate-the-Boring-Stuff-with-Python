# searchpypi.py - Opens several search results.
import requests, webbrowser, bs4, sys

print("Searching")
res = requests.get("https://pypi.org/search?q=" + " ".join(sys.argv[1:]))
print(res.status_code)


# Reterive top search result links
soup = bs4.BeautifulSoup(res.text, "html.parser")

# open a browser tab for each result
linkElems = soup.select(".package-snippet")
numOpen = min(2, len(linkElems))
for i in range(numOpen):

    url = "https://pypi.org" + linkElems[i].get("href")
    print("Opening....", url)
    webbrowser.open(url)

# Error
"""
Webbrowser not opening ???
solution first . open a new chrome browser by clicking on icon . when you restore chrome broswer
your system lost the track of broswer and they are not registered in the main memory

2. if is still no working register chrome.exe to webbrowser module

import os , webbrowser
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)

"""

