'''
    供应商信息页面对象
'''
from Day11.pom_unittest.base_page.base_page import BasePage


class VendorPage(BasePage):
    # 页面url
    url = 'http://39.101.122.147:3000/system/vendor'

    # 页面核心元素：与操作流程相关联的元素，其余元素不需要。
    vendor_add = ('xpath', '//div[@class="table-operator"]/button[1]')  # 元素核心内容包括定位方法以及对应的value
    supplier_name = ('id', 'supplier')
    supplier_telephone = ('id', 'telephone')
    supplier_save = ('xpath', '//div[@class="ant-modal-footer"]/div[1]/button[2]')

    search_name = ('xpath', '//input[@placeholder="请输入名称查询"]')
    search_button = ('xpath', '//span[text()="查 询"]/..')

    # 页面的子流程封装
    def add_supplier(self, name, tele):
        self.open_url(self.url)
        self.click(*self.vendor_add)
        self.input(*self.supplier_name, text=name)
        self.input(*self.supplier_telephone, text=tele)
        self.click(*self.supplier_save)
        self.wait(3)

    def search(self, name):
        self.open_url(self.url)
        self.input(*self.search_name, text=name)
        self.click(*self.search_button)
