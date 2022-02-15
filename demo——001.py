# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
#
# driver.set_window_size(800,600)
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
#
# js = "window.scrollTo(100,450);"

# 按照设置的格式打印cookie
# from selenium import webdriver
# import time
#
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
#
# cookie = driver.get_cookies()
# driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbbbbb'})
# for cookie in driver.get_cookies():
#     print("%s ->%s"% (cookie['name'], cookie['value']))

# 未完成，多窗口切换，百度账号登录，注册账号无法点击
# from selenium import webdriver
# import time
#
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
#
# search_windows = driver.current_window_handle
#
# driver.find_element_by_link_text('登录').click()
# driver.find_element_by_class_name("pass-reglink pass-link").click()
#
# all_handles = driver.window_handles
#
# for handle in all_handles:
#     if handle != search_windows:
#         driver.switch_to.window(handle)
#         print(driver.title)
#         driver.find_element_by_name("username").send_keys('username')
#         driver.find_element_by_name('password').send_keys('123456789')
#         time.sleep(2)
#
#         driver.close()
#
# driver.switch_to.window(search_windows)
# print(driver.title)
#
# driver.quit()

# from time import sleep
#
# # 使用切换表单的形式进行QQ邮箱的登录，程序进行到滑动验证
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Firefox()
# driver.get("https://mail.qq.com/")
# sleep(2)
#
# driver.switch_to.frame("login_frame")
# driver.find_element_by_id("u").send_keys("1492517451")
# driver.find_element_by_id("p").send_keys("RONALDO.TE")
# sleep(2)
# driver.find_element_by_xpath('//*[@id="login_button"]').send_keys(Keys.ENTER)
# sleep(3)
# driver.switch_to.default_content()
#
# driver.quit()

# from selenium import webdriver  #利用Xpath匹配一组元素
# from time import sleep
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("安静")
# driver.find_element_by_id("su").send_keys(Keys.ENTER)
#
# sleep(2)
#
# texts = driver.find_elements_by_xpath('//*[@class="c-title t" or @class="c"]/a')
# print(len(texts))
#
# for t in texts:
#     print(t.text)
#
# driver.quit()

# from selenium import webdriver  #利用Xpath定位元素，完成悬停
# from time import sleep
# from selenium.webdriver import ActionChains
#
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
#
# above = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
#
# ActionChains(driver).move_to_element(above).perform()
# sleep(3)
# driver.quit()

# from selenium import webdriver  #打印网页信息
# from time import sleep
#
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
#
# size = driver.find_element_by_id('kw').size
# print(size)
#
# text = driver.find_element_by_xpath("//html/body/div[1]/div[1]/div[7]/div").text
# print(text)
#
# attributes = driver.find_element_by_id('kw').get_attribute('type')
# print(attributes)
#
# result = driver.find_element_by_id('kw').is_displayed()
# print(result)
#
# driver.quit()

# from selenium import webdriver #页面前进后退
# from time import sleep
#
# driver=webdriver.Firefox()
# driver.get("http://www.baidu.com")
# sleep(3)
# driver.get("http:www.taobao.com")
# driver.back()
# sleep(3)
# driver.forward()
# sleep(3)
# driver.quit()
#
# from time import sleep
#
# from selenium import webdriver  # 利用By定位元素
#
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com/")
#
# driver.find_element(By.NAME, "wd").send_keys("selenium")
# driver.find_element(By.CLASS_NAME, "s_ipt").send_keys("ming")
# driver.find_element(By.ID, "kw").send_keys("广州恒太")
# sleep(3)
#
# driver.quit()

# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
#
# driver.find_element_by_id("kw") .send_keys("selenium")
# driver.find_element_by_id("su") .click()
# sleep(2)
#
# texts = driver.find_element_by_xpath("//div[@tp1='se_com_default']")
#
# print(len(texts))
#
# for i in texts:
#     print(i.texts)
#
# driver.quit()

# '''按键操作'''
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep
#
# driver = webdriver.Firefox()
# driver.get('http://www.baidu.com/')
#
# driver.find_element_by_id("kw") .send_keys("selenium")
# sleep(5)
# driver.find_element_by_id("kw") .send_keys(Keys.BACK_SPACE)
# sleep(3)
# driver.find_element_by_id("kw") .send_keys(Keys.SPACE)
# driver.find_element_by_id("kw") .send_keys("教程")
# driver.find_element_by_id("su").click()
# sleep(4)
# driver.quit()

# '''鼠标悬停操作  百度首页测试，右侧更多成功，左侧设置失败'''
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
#
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# above = driver.find_element_by_link_text("更多")
# ActionChains(driver).move_to_element(above).perform()
# # hideern_submenu = driver.find_element_by_id("lg #submenu")
# # ActionChains(driver).move_to_element(above).click(hideern_submenu).perform()
#
# sleep(10)
# driver.quit()

# from selenium import webdriver  //JS 报错
# from time import sleep
# js="window.open('{}','_blank');"
# driver = webdriver.Firefox()
#
# driver.get('http://www.baidu.com')
# now_url = driver.current_url
# print("URL:" + now_url)
#
# driver.execute_script("http://news.baidu.com/")
# driver.switch_to.window(driver.window_handles[-1])
# now_url2 = driver.current_url
# print("URL:" + now_url2)
# driver.quit()

# driver.set_window_size(480,800)
# sleep(10)
# driver.quit()

# import sys
# from os.path import dirname, abspath
#
# project_path = dirname(dirname(abspath(__file__)))
# sys.path.append(project_path + "\\test1")
# from unittest import add
#
# print(add(2,3))

# import sys
# print(sys.path)

# from time import sleep as sys_sleep
#
# def sleep(sec):
#     print("this is i defined sleep()")

# from time import ctime,sleep
# print(ctime())
# sleep(2)
# print(ctime())

# class A:  //继承：B继承A
#     def __init__(self, a, b):
#         self.a = int (a)
#         self.b = int (b)
#
#     def add(self):
#         return self.a+self.b
# '''count = A('4',5)'''
# class B(A):
#
#     def sub(self, a, b):
#         return a - b
# print(B(2,3).add())