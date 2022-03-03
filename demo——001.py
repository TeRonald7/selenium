from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.baidu.com")
driver.find_element_by_id("su").send_keys("selenium")
