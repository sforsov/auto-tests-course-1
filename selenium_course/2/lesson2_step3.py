from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def sum(x, y):
    return str(x + y)

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)
try:
	
    n = sum(int(browser.find_element_by_css_selector('#num1').text),int(browser.find_element_by_css_selector('#num2').text))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(n)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()