from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	browser.execute_script("window.scrollBy(0, 200);")

	price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
	button1 = browser.find_element_by_tag_name("#book")
	button1.click()
	browser.execute_script("window.scrollBy(0, 200);")

	x_element = browser.find_element_by_tag_name("#input_value")
	x = x_element.text
	y = calc(x)

	input1 = browser.find_element_by_tag_name("#answer")
	input1.send_keys(y)
	button2 = browser.find_element_by_tag_name("#solve")
	button2.click()


finally:
    time.sleep(5)
    browser.quit()