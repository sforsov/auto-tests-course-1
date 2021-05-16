from selenium import webdriver
import pytest
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('test_number', ["236895","236896","236897","236898","236899","236903","236904","236905"])
class TestMainPage1():
    def test_1(self, browser, test_number):
        link = f"https://stepik.org/lesson/{test_number}/step/1"
        browser.get(link)
        answer = math.log(int(time.time()))
        time.sleep(3)
        text_area = browser.find_element_by_css_selector("textarea.textarea").send_keys(str(answer))
        button = browser.find_element_by_css_selector("button.submit-submission").click()
        time.sleep(2)
        message = browser.find_element_by_css_selector("pre.smart-hints__hint").text
        example_text = "Correct!"
        assert message == example_text, "Wrong answer"