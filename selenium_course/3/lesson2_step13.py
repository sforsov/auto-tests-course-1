from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):


    def test_abs1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)

    
        input1 = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("input[placeholder='Input your email']")
        input3.send_keys("1@1.ru")
        input4 = browser.find_element_by_css_selector("input[placeholder='Input your phone:']")
        input4.send_keys("+79000000000")
        input5 = browser.find_element_by_css_selector("input[placeholder='Input your address:']")
        input5.send_keys("Russia")
    
    
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    
        time.sleep(1)

    
        welcome_text_elt = browser.find_element_by_tag_name("h1")
    
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!") 


        time.sleep(2)
        browser.quit()

    def test_abs2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)

    
        input1 = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("input[placeholder='Input your email']")
        input3.send_keys("1@1.ru")
        input4 = browser.find_element_by_css_selector("input[placeholder='Input your phone:']")
        input4.send_keys("+79000000000")
        input5 = browser.find_element_by_css_selector("input[placeholder='Input your address:']")
        input5.send_keys("Russia")
    
    
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)
    
        welcome_text_elt = browser.find_element_by_tag_name("h1")
    
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!") 

        time.sleep(2)
        browser.quit()

if __name__ == "__main__":
    unittest.main()
