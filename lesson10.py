from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, "div.form-group>input[name='firstname']")
input1.send_keys("Ivan")
input2 = browser.find_element(By.CSS_SELECTOR,"div.form-group>input[name='lastname']")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CSS_SELECTOR,"div.form-group>input[name='email']")
input3.send_keys("Smolensk")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "10.txt"
file_path = os.path.join(current_dir, file_name)
input4 = browser.find_element(By.ID,"file")
input4.send_keys(file_path)
browser.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()