from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base():
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def FindElement(self, locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型（“id", "value")')
        else:
            print("正在定位元素信息:定位方式->%s, value值->%s" % (locator[0], locator[1]))

            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    def sendKeys(self, locator, text):
        ele = self.FindElement(locator)
        ele.send_keys(text)

    def click(self, locator):
        ele = self.FindElement(locator)
        ele.click()

    def is_text_exist(self, locator, _text):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False

    def is_alert(self):
        self.a = self.driver.switch_to_alert()
        text = self.a.text
        print(text)
        self.a.accept()

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
    loc_user = ("id", "account")
    loc_psw = ("name", "password")
    loc_submit = ("id", "submit")

    a = Base(driver)
    a.sendKeys(loc_user, "admin111")
    a.sendKeys(loc_psw, "123456")
    a.click(loc_submit)
    time.sleep(2)
    a.is_alert()

