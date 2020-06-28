# keep playing the 2048 in a loop as long as the for loop is not exhausted

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://gabrielecirulli.github.io/2048/")
htmlElem = browser.find_element_by_tag_name("html")
for i in range(100):
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
    try:
        elem = browser.find_element_by_css_selector(
            "body > div.container > div.game-container > div.game-message.game-over"
        )
        if "Game over!" in elem.text:
            tryagain = browser.find_element_by_link_text("Try again")
            tryagain.click()
            # print('Found <%s> element with that class name!' % (elem.tag_name))
    except:
        pass

