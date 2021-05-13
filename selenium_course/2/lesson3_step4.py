from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button1 = browser.find_element_by_css_selector("button.btn").click()
    confirm = browser.switch_to.alert.accept()
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input1 = browser.find_element_by_id("answer").send_keys(y)
    button2 = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()