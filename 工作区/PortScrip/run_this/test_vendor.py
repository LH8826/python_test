import datetime
import time
import requests
import json
from Test.PortScrip.common.MysqlHelper import *
import operator
import xlrd
import xlwt
import xlutils
class Test_vendor():
    def test_vendor(self):
        #读取文件
        book = xlrd.open_workbook(r'E:\pycharm文件存放\测试\PortScrip\data\vendor.xlsx')
        sheet = book.sheet_by_name('Sheet1')
        col = sheet.col_values(1)
        row = sheet.row_values(1)
        print(row)
if __name__ == '__main__':
    a = Test_vendor
    a.test_vendor()