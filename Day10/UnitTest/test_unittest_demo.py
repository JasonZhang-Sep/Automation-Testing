import unittest


class TestDemo(unittest.TestCase):
    demo = None
    # 类级级别前置与后置
    @classmethod
    def setUpClass(cls):
        print('类级别前置')

    @classmethod
    def tearDownClass(cls):
        print('类级别后置')

    # 用例级别前置与后置
    # def setUp(self):
    #     print('用例级别前置')
    #
    # def tearDown(self):
    #     print('用例级别后置')

    # 测试用例
    def test_case01(self):
        print('这是第一条case')
        1 / 0

    def test_case(self):
        print('这是第二条case')
        TestDemo.demo = 1  # 属性赋值实现数据互通，但是要注意unittest的执行顺序

    def test_case03(self):
        print('这是第三条case')
        print(self.demo)
        assert 1 == 3, '断言失败，测试不通过'

    def test_case04(self):
        print('这是第四条case')

if __name__ == '__main__':
    unittest.main()