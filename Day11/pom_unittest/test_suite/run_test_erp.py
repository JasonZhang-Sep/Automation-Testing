import HTMLTestRunner
import os
import time
import unittest

current_file = os.path.abspath(__file__)  # 获取当前Python脚本文件的绝对路径,.../pom_unittest/test_suite/run_test_erp.py
root_dir = os.path.dirname(os.path.dirname(current_file))  # 得到: .../pom_unittest
path = os.path.join(root_dir,'test_cases')

discover = unittest.defaultTestLoader.discover(start_dir=path,
                                               pattern='test_erp_login.py')

report_dir = '../report/'
timestamp = time.strftime('%Y%m%d_%H%M%S')
report_file = report_dir + f'report_{timestamp}.html'
report_title = '这是测试报告标题'
report_description = '这是测试报告的描述'
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

with open(report_file, 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           title=report_title,
                                           description=report_description,
                                           verbosity=2)
    runner.run(discover)