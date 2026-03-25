import pytest


class TestDemo:

    @pytest.mark.test01
    @pytest.mark.login
    def test_demo_01(self):
        print("test_demo01")

    def test_demo_02(self):
        print("test_demo02")


if __name__ == '__main__':
    pytest.main(['-sv', 'test_mark.py', '-m' 'test01'])