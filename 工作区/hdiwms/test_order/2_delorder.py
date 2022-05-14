import datetime
import time
import requests
import json
from common.MysqlHelper import *
import decimal
import pytest
import allure



class TestClass_DelOrder():
    def test_delorder(self,fixorder):
        # 以下是删除订单
        #查找定单uuid和版本
        vsourceBillNumber = fixorder
        vdcUuid = '000002010000001'
        helper = MysqlHelper('db2.iwms.hd123.cn', 3306, 'iwms', 'iwms', 'iwmsfacility')
        # 执行sql语句
        sqlmst = "select uuid,fversion " \
         "from iwmsorderbill where  sourceBillNumber = '%s'"%vsourceBillNumber + " and dcUuid = '%s'"  %vdcUuid
        # print(sqlmst)
        ordermst = helper.get_all(sqlmst)  # 执行sql语句，返回sql查询成功的记录数目
        vuuid = ordermst[0][0]
        data = {
            'version': ordermst[0][1]
        }
        # vversion = ordermst[0][1]
        # print(vuuid,vversion,type(vversion))
        #从接口删除定单
        # url = 'http://app2.iwms.hd123.cn:8081/test/iwms-facility/facility/order/%s' %vuuid+'?version=%s' %vversion
        url = 'http://app2.iwms.hd123.cn:8081/test/iwms-facility/facility/order/%s' %vuuid
        headers = {'content-type': "application/json", 'check_flag': 'false'}
        response = requests.delete(url,params=data,headers=headers)
        print(response.status_code)
        assert response.status_code == 200
        # print (response.text)
        r1 = response.json()
        print (r1)
        r3 = r1['success']
        if r3 == True:
            print('删除成功')
        else:
            print('删除失败','错误信息为:'+ r1['message'])

        helper = MysqlHelper('db2.iwms.hd123.cn', 3306, 'iwms', 'iwms', 'iwmsfacility')
        # 数据库查询
        sqlmst = "select * from iwmsorderbill where  sourceBillNumber = '%s'"%vsourceBillNumber + " and dcUuid = '%s'"  %vdcUuid
        # print(sqlmst)
        res = helper.get_one(sqlmst)  # 执行sql语句，返回sql查询成功的记录数目
        print(res)

        if res != None:
            print('从数据库删除失败')
        else:
            print('从数据库删除成功')
            print(vsourceBillNumber)
#
# if __name__ == '__main__':
#     pytest.main(['-s','-q','D:/pycharm/test/hdiwms/test_order/2_delorder.py','--alluredir D:/Alice/jieguo'])
