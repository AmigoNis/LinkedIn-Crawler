#! /user/bin/python
"""

"""

import time
from selenium import webdriver
from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys

start_time = time.time()
driver = webdriver.Firefox()
d = driver.get('http://www.ynet.co.il')
print driver.title
page = driver.page_source
BeautifulSoup.prettify()

print round(time.time()-start_time, 2), " seconds total."
