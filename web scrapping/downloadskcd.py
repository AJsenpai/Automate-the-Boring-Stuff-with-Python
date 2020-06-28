# downloadXkcd.py - Downloads every single XKCD comic.
import requests, os, bs4

url = "https://xkcd.com/2066"
# exist_ok=True ; if already exists won't throw an error
os.makedirs("c:/Users/Jai/Desktop/Docs/xkcd", exist_ok=True)
xkcd_folder = os.path.abspath("c:/Users/Jai/Desktop/Docs/xkcd")
while not url.endswith("#"):  # most recent page
    # download the page
    print(f"downloading page... {url} ")
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # find the url of the comic page
    comicElem = soup.select("#comic img")
    if comicElem == []:
        print("couldn't find comic image")
    else:
        comicUrl = "https:" + comicElem[0].get("src")
        # download the image
        print(f"Downloading image... {url}")
        res = requests.get(comicUrl)
        res.raise_for_status()

        # save the images to xkcd folder
        with open(
            os.path.join(xkcd_folder, os.path.basename(comicUrl)), "wb"
        ) as imageFile:
            for chunk in res.iter_content(100000):  # image_data = 100000 bytes each
                imageFile.write(chunk)
    prevLink = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com" + prevLink.get("href")
print("Done")


# The call os.makedirs() ensures that this folder exists,and the exist_ok=True keyword argument prevents the function from throwing
# an exception if this folder already exists.
