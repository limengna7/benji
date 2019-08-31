from common import HTMLTestRunner_cn
import unittest
import time

casepath = "C:\\Users\\Admin\\.PyCharm50\\webAuto\\"
#discover 可以加载多个用例

discover = unittest.defaultTestLoader.discover(start_dir=casepath,
                                               pattern='test*.py',
                                               top_level_dir=None)
print(discover)

now = time.strftime("%Y_%m_%d_%H_%M_%S")
filename = "C:\\Users\\Admin\\.PyCharm50\\webAuto\\report\\"+now+"report.html"

fp = open(filename, "wb")

runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                          title="测试报告",
                                          description="执行用例情况")
runner.run(discover)
fp.close()


