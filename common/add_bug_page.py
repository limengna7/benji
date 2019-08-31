from common.Base import Base
from selenium import webdriver
import time
from common.LogIn import Log_In


class Add_Bug(Base):

    loc_test = ("link text", "测试")
    loc_BUG = ("link text", "Bug")
    loc_add_bug = ("xpath", ".//*[@id='createActionMenu']/a")
    loc_click_trunk = ("xpath", ".//*[@id='openedBuild_chosen']/ul")
    loc_add_trunk = ("xpath", ".//*[@id='openedBuild_chosen']/div/ul/li")
    loc_title = ("id", "title")
    loc_save = ("id", "submit")
    loc_name = ("xpath", ".//*[@id='bugList']/tbody/tr[1]/td[4]/a")


    def add_bug(self, title):
        self.click(self.loc_test)
        self.click(self.loc_BUG)
        self.click(self.loc_add_bug)
        self.click(self.loc_click_trunk)
        self.click(self.loc_add_trunk)
        self.sendKeys(self.loc_title, title)
        js = 'document.getElementsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML="hello world";'
        self.driver.execute_script(js)
        self.click(self.loc_save)

    def is_add_success(self, text):
        return self.is_text_exist(self.loc_name, text)

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
    driver.maximize_window()

    Log_In(driver).log_in_page(user="admin", psw="123456")

    timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    title = "test BUG"+timestr
    print(title)
    a = Add_Bug(driver)
    a.add_bug(title)
    time.sleep(2)
    result = a.is_add_success(title)
    print(result)