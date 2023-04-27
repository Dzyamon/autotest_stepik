from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os
from faker import Faker


link1 = "http://suninjuly.github.io/simple_form_find_task.html"
link2 = "http://suninjuly.github.io/find_link_text"
link3 = "http://suninjuly.github.io/huge_form.html"
link4 = "http://suninjuly.github.io/find_xpath_form"
link5 = "http://suninjuly.github.io/registration1.html"
link6 = "http://suninjuly.github.io/registration2.html"
link7 = "https://suninjuly.github.io/math.html"
link8 = "http://suninjuly.github.io/get_attribute.html"
link9 = "http://suninjuly.github.io/selects1.html"
link10 = "http://suninjuly.github.io/execute_script.html"
link11 = "http://suninjuly.github.io/file_input.html"
link12 = "http://suninjuly.github.io/alert_accept.html"
link13 = "http://suninjuly.github.io/redirect_accept.html"
link14 = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link14)
# fake = Faker()

try:
    # #link1
    # input1 = browser.find_element(By.TAG_NAME, "input")
    # input1.send_keys("Ivan")
    # input2 = browser.find_element(By.NAME, "last_name")
    # input2.send_keys("Petrov")
    # input3 = browser.find_element(By.CLASS_NAME, "city")
    # input3.send_keys("Smolensk")
    # input4 = browser.find_element(By.ID, "country")
    # input4.send_keys("Russia")
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()

    # #link2
    # x = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    # browser.find_element(By.PARTIAL_LINK_TEXT, x).click()

    # #link3
    # elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    # #v2
    # elements = browser.find_elements(By.TAG_NAME, "input")
    # for element in elements:
    #     element.send_keys(fake.name())

    # #link4
    # input1 = browser.find_element(By.TAG_NAME, "input")
    # input1.send_keys("Ivan")
    # input2 = browser.find_element(By.NAME, "last_name")
    # input2.send_keys("Petrov")
    # input3 = browser.find_element(By.CLASS_NAME, "city")
    # input3.send_keys("Smolensk")
    # input4 = browser.find_element(By.ID, "country")
    # input4.send_keys("Russia")
    # button = browser.find_element(By.XPATH, "//button[text()='Submit']") # //*[@type="submit"]
    # button.click()

    # # #link5
    # browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input").send_keys("A")
    # # "first_block .form-control.first"
    # browser.find_element(By.CSS_SELECTOR, ".first_block :nth-child(2) input").send_keys("B")
    # browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("C")
    # #browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("C")
    #     browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    # time.sleep(1)
    # welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    # assert "Congratulations! You have successfully registered!" == welcome_text

    # #link7
    # def calc(x):
    #     return str(math.log(abs(12 * math.sin(int(x)))))
    # browser.find_element(By.ID, "robotCheckbox").click()  # By.CSS_SELECTOR, "#robotCheckbox"
    # browser.find_element(By.ID, "robotsRule").click()
    # x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    # x = x_element.text
    # y = calc(x)
    # browser.find_element(By.ID, "answer").send_keys(y)
    # browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # #link8
    # def calc(x):
    #     return str(math.log(abs(12 * math.sin(int(x)))))
    # browser.find_element(By.ID, "robotCheckbox").click()
    # browser.find_element(By.ID, "robotsRule").click()
    # chest = browser.find_element(By.ID, "treasure")
    # x = chest.get_attribute("valuex")
    # y = calc(x)
    # browser.find_element(By.ID, "answer").send_keys(y)
    # browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # #link9
    # a = browser.find_element(By.ID, "num1").text
    # b = browser.find_element(By.ID, "num2").text
    # z = int(a) + int(b)
    # Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(str(z))
    # browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    # #.select_by_visible_text("Python") #.select_by_index(1) c 0 начало
    # # #v2
    # # browser.find_element(By.TAG_NAME, "select").click()
    # # browser.find_element(By.CSS_SELECTOR, "[value='1']").click()

    #browser.execute_script("document.title='Script executing';alert('Robots at work');")

    # #link10 - button not visible
    # def calc(x):
    #     return str(math.log(abs(12 * math.sin(int(x)))))
    # x = browser.find_element(By.ID, "input_value").text
    # y = calc(x)
    # browser.find_element(By.ID, "answer").send_keys(y)
    # browser.find_element(By.ID, "robotCheckbox").click()
    # button = browser.find_element(By.TAG_NAME, "button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # browser.find_element(By.ID, "robotsRule").click()
    # button.click()

    # #link11
    # browser.find_element(By.NAME, "firstname").send_keys("A")
    # browser.find_element(By.NAME, "lastname").send_keys("B")
    # browser.find_element(By.NAME, "email").send_keys("C")
    # with open("file.txt", "w") as file:
    #     content = file.write("automationbypython")  # create test.txt file
    # current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    # browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
    # browser.find_element(By.TAG_NAME, "button").click()
    # #browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # #link12 - pop-up window
    # def calc(x):
    #     return str(math.log(abs(12 * math.sin(int(x)))))
    # browser.find_element(By.TAG_NAME, "button").click()
    # browser.switch_to.alert.accept()
    # x = browser.find_element(By.ID, "input_value").text
    # y = calc(x)
    # browser.find_element(By.ID, "answer").send_keys(y)
    # browser.find_element(By.TAG_NAME, "button").click()

    # #link13 - new tab
    # def calc(x):
    #     return str(math.log(abs(12 * math.sin(int(x)))))
    # browser.find_element(By.TAG_NAME, "button").click()
    # browser.switch_to.window(browser.window_handles[1])
    # x = browser.find_element(By.ID, "input_value").text
    # y = calc(x)
    # browser.find_element(By.ID, "answer").send_keys(y)
    # browser.find_element(By.TAG_NAME, "button").click()

    # #link14 - explicit wait for value
    # def calc(x):
    #     return str(math.log(abs(12 * math.sin(int(x)))))
    # WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    # browser.find_element(By.ID, "book").click()
    # x = browser.find_element(By.ID, "input_value").text
    # y = calc(x)
    # browser.find_element(By.ID, "answer").send_keys(y)
    # browser.find_element(By.ID, "solve").click()

# except Exception as error:
#     print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    print(browser.switch_to.alert.text.split(': ')[-1])
    time.sleep(5)
    browser.quit()