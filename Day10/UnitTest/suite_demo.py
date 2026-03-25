import HTMLTestReportCN
import os
import time
import unittest
import HTMLTestRunner

# 创建套件
suite = unittest.TestSuite()
# 添加测试用例
'''
# 获取脚本的相对路径,report
current_file = os.path.abspath(__file__)
# 从脚本位置逐级向上获取项目根路径,UnitTest->Day10->UI_Auto
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
# 拼接目标路径
path = os.path.join(root_dir, 'Day11', 'DDT')
'''

path = '../../Day11/DDT'
# 基于discover来实现用例的添加,默认返回一个套件
discover = unittest.defaultTestLoader.discover(start_dir=path,         # 获取用例的起始路径
                                               pattern='ddt_demo.py')    # 获取用例的匹配规则

# 套件的运行
# runner = unittest.TextTestRunner(verbosity=2)  # 2表示最详细的信息记录
# runner.run(discover)

# 测试报告
report_dir = './report/'  # 测试报告保存路径
timestamp = time.strftime('%Y%m%d_%H%M%S')
report_file = report_dir + f'report_{timestamp}.html'  # 测试报告名称，有需要可以自行添加时间戳
report_title = '这是测试报告标题'
report_description = '这个是测试报告的描述'

report_tester = '张杰'  # 测试者，reportCN中额外的参数

# 判断测试报告保存路径是否存在，不存在则创建
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

# 测试报告生成
with open(report_file, 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           title=report_title,
                                           description=report_description,
                                           verbosity=2)

    # runner = HTMLTestReportCN.HTMLTestRunner(stream=file,
    #                                          title=report_title,
    #                                          description=report_description,
    #                                          tester=report_tester,
    #                                          verbosity=2)

    runner.run(discover)
