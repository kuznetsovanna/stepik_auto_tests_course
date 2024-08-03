from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_el=browser.find_element(By.ID,'num1')
x=int(x_el.text)
y_el=browser.find_element(By.ID,'num2')
y=int(y_el.text)
summ=x+y
summ=str(summ)

select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_visible_text(summ)
browser.find_element(By.TAG_NAME,'button').click()
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()

