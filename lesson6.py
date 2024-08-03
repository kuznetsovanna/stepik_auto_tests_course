from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_el=browser.find_element(By.ID,'input_value')
x=x_el.text
y=calc(x)
in1=browser.find_element(By.ID,'answer')
in1.send_keys(y)
print('in1',in1)
cb=browser.find_element(By.CSS_SELECTOR,'div.form-check-custom>input')
print(cb,'dfgdfg')
cb.click()
time.sleep(3)
radio=browser.find_element(By.ID,'robotsRule')
radio.click()
btn=browser.find_element(By.CLASS_NAME,'btn-default')
btn.click()
# ожидание чтобы визуально оценить результаты прохождения скрипта
       


