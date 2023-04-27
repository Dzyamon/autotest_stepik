import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestForms(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def fill_form(self, url):
        browser = self.driver
        browser.implicitly_wait(5)
        browser.get(url)
        browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input").send_keys("Petrov")
        browser.find_element(By.CLASS_NAME, "form-control.third").send_keys("url@gmail")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        return browser.find_element(By.TAG_NAME, "h1").text

    def test_registration1(self):
        form_url = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(form_url)
        self.assertEqual("Congratulations! You have successfully registered!",
                         registration_result)

    def test_registration2(self):
        form_url = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(form_url)
        self.assertEqual("Congratulations! You have successfully registered!",
                         registration_result)


if __name__ == '__main__':
    unittest.main()