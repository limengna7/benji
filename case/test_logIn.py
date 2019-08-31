from selenium import webdriver
from common.Base import Base
from common.LogIn import Log_In
import unittest
import ddt

testdata = [{"user":"admin","psw":"123456","expect":True},
        {"user":"adminxx", "psw":"123456", "expect":False},
        {"user":"admin", "psw":"12111", "expect":False}]

@ddt.ddt
class Test_logIn(unittest.TestCase):

    loc_name = ("xpath", ".//*[@id='userMenu']/a")


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.b = Base(cls.driver)

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.get("http://127.0.0.1:81/zentao/user-login.html")

    def log_in_case(self, user="admin", psw="123456", expect=True):
        Log_In(self.driver).log_in_page(user, psw)
        result = self.b.is_text_exist(self.loc_name, user)
        print(result)
        expect_result = expect
        self.assertEqual(result, expect_result)

    @ddt.data(*testdata)
    def test_01(self, data):
        '''测试登陆页面'''
        print("-----------Test Start-----------")
        print("the test data is %s"%data)
        self.log_in_case(data["user"], data["psw"], data["expect"])
        print("-----------Test End-------------")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

