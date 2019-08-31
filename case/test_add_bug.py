from selenium import webdriver
import time
from common.LogIn import Log_In
from common.add_bug_page import Add_Bug
import unittest

class Test_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
        Log_In(cls.driver).log_in_page(user="admin", psw="123456")
        cls.a = Add_Bug(cls.driver)

    def test_01(self):
        '''添加bug并验证bug添加成功'''
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "test BUG"+timestr
        self.a.add_bug(title)
        time.sleep(3)
        result = self.a.is_add_success(title)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()