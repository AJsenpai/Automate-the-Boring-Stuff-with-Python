# Modyfing the original xkcd downloader from webscrapping
# Using Threads to download range of comics at the same time
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4, threading

# url = "https://xkcd.com/2066"
# exist_ok=True ; if already exists won't throw an error
os.makedirs("c:/Users/Jai/Desktop/Docs/xkcd_Thread", exist_ok=True)


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print(f"Downloading page https://xkcd.com/{urlNumber}....")
        res = requests.get(f"https://xkcd.com/{urlNumber}")
        res.raise_for_status()
        xkcd_folder = os.path.abspath("c:/Users/Jai/Desktop/Docs/xkcd_Thread")

        soup = bs4.BeautifulSoup(res.text, "html.parser")
        # find the url of the comic page
        comicElem = soup.select("#comic img")
        if comicElem == []:
            print("couldn't find comic image")
        else:
            comicUrl = comicElem[0].get("src")
            # download the image
            print(f"Downloading image... {comicUrl}")
            res = requests.get("https:" + comicUrl)
            res.raise_for_status()

            # save the images to xkcd folder
            with open(
                os.path.join(xkcd_folder, os.path.basename(comicUrl)), "wb"
            ) as imageFile:
                for chunk in res.iter_content(100000):  # image_data = 100000 bytes each
                    imageFile.write(chunk)
    print("Done")


# create and start the Thread objects
downloadThreads = []  # a list of all the thread objects
for i in range(0, 140, 10):  # loop 14 times create 14 thread
    start = i
    end = i + 9
    if start == 0:
        start = 1  # there is no comic at 0 so set it to 1
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# wait for all the threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print("Done.")
