from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.TAG_NAME,'button').click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x_el=browser.find_element(By.ID,'input_value')
x=float(x_el.text)
y=math.log(abs(12*math.sin(x)))

input1=browser.find_element(By.ID,'answer')
input1.send_keys(y)
browser.find_element(By.TAG_NAME,'button').click()

print(browser.switch_to.alert.text)

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()


