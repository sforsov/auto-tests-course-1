from selenium import webdriver
import time
import os
current_dir = os.path.abspath(os.path.dirname(__file__))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname").send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname").send_keys("Petrov")
    input3 = browser.find_element_by_name("email").send_keys("123@321.fg")
	
	
    file_path = os.path.join(current_dir, 'name.txt')
    select_file_button = browser.find_element_by_css_selector('#file')
    select_file_button.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(7)
    browser.quit()