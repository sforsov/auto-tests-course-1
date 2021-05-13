from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector("button.trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x =  browser.find_element_by_id("input_value").text
    input1 =  browser.find_element_by_id("answer").send_keys(calc(x))
    button2 =  browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()