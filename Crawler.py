#! /user/bin/python
"""
A simple LinkedIn crawler based on DrapsTV video: https://www.youtube.com/watch?v=twRQNSFXiYs
"""

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

sleep_time = 3


def get_people(page):
    links = set()
    for link in page.findAll('h3'):
        for link in link.findAll('a'):
            if '/profile/view?id=' in str(link.get('href')):
                # print str(link.get('href'))
                links.add(str(link.get('href')))
    return links





def main():
    print "Please input your LinkedIn credentials: "
    my_email = raw_input("Email >>> ")
    my_pass = raw_input("Pass >>>")
    my_search = raw_input("Search string >>> ")
    start_time = time.time()
    browser = webdriver.Firefox()
    browser.get('https://www.linkedin.com/uas/login')

    email_field = browser.find_element_by_id('session_key-login')
    email_field.send_keys(my_email)
    pass_field = browser.find_element_by_id('session_password-login')
    pass_field.send_keys(my_pass)
    pass_field.submit()
    time.sleep(sleep_time)
    search_field = browser.find_element_by_id('main-search-box')
    search_field.send_keys(my_search)
    search_field.submit()
    search_page = BeautifulSoup(browser.page_source, 'html.parser')
    # print search_page.prettify()
    links = get_people(search_page)
    for link in links:
        print link


    print "-------------- Total time: ", round(time.time()-start_time-sleep_time, 2), '--------------'








if __name__ == "__main__":
    main()

