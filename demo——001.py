from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element(By.ID , "kw").send_keys("lil")
sleep(3)
driver.quit()
