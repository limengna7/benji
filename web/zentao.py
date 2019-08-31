from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")

driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_id("submit").click()