# get the weather forecast detail for given zip code
import requests
import bs4

res = requests.get(
    "https://forecast.weather.gov/MapClick.php?lat=37.786992017825476&lon=-122.40028632619556"
)
res.raise_for_status()
data = bs4.BeautifulSoup(res.text, "html.parser")
# text = data.findAll(text=True)
elements = data.select("#detailed-forecast")
for text in elements[0].find_all(text=True):
    print(text)


# # elements = data.select('#detailed-forecast')
# text = data.get_text()

# # break into lines and remove leading and trailing space on each
# lines = (line.strip() for line in text.splitlines())

# # break multi-headlines into a line each
# chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

# # drop blank lines
# text = '\n'.join(chunk for chunk in chunks if chunk)
