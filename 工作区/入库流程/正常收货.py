# coding = utf-8
import requests
import json
import xlrd
class ExcelData():
    def readeFile(self):
        books = xlrd.open_workbook('E:\jmter_Folder\iwms_jmeter\iwmsreceive\OrderbillNumber.csv','rt')#打开文件
        sheet = books.sheet_by_name('OrderbillNumber')
        cow_list = sheet.cow_values(0)[0:1]
        print(cow_list)


if __name__ == '__main__':
   a = ExcelData()
   a.readeFile()