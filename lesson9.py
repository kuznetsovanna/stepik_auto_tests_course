from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_el=browser.find_element(By.ID,'input_value')
x=float(x_el.text)
y=math.log(abs(12*math.sin(x)))
inp=browser.find_element(By.ID,'answer')
inp.send_keys(y)
button = browser.find_element(By.TAG_NAME,'button')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.find_element(By.ID,'robotCheckbox').click()
browser.find_element(By.ID,'robotsRule').click()
button.click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()