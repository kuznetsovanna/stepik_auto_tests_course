from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link) 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_el=browser.find_element(By.ID,'treasure')
x=x_el.get_attribute('valuex')
y=calc(x)
in1=browser.find_element(By.ID,'answer')
in1.send_keys(y)
cb=browser.find_element(By.ID,'robotCheckbox')
cb.click()
time.sleep(3)
radio=browser.find_element(By.ID,'robotsRule')
radio.click()
btn=browser.find_element(By.CLASS_NAME,'btn-default')
btn.click()
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()


