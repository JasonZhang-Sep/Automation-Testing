import os
import time
import unittest
import HTMLTestRunner


# 获取脚本的相对路径,report
current_file = os.path.abspath(__file__)
# 从脚本位置逐级向上获取项目根路径,UnitTest->Day10->UI_Auto
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
# 拼接目标路径
# path = os.path.join(current_file)
path = os.path.dirname(current_file)


discover = unittest.defaultTestLoader.discover(start_dir=path,       # 获取用例的起始路径
                                               pattern='test_erp_login.py')
# 测试报告
report_dir = './report/'
timestamp = time.strftime('%Y%m%d_%H%M%S')
report_file = report_dir + f'report_{timestamp}.html'
report_title = '这是测试报告标题'
report_description = '这是测试报告的描述'
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

# 测试报告生成
with open(report_file, 'wb') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                           title=report_title,
                                           description=report_description,
                                           verbosity=2)
    runner.run(discover)


