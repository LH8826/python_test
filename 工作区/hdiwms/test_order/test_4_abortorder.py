import datetime
import time
import requests
import json
from common.MysqlHelper import *
import decimal
import pytest
import allure

class TestClass_AbortOrder():
    def test_abortorder(self,fixorder):
        # 以下是查找订单
        data = {
            'sourceBillNumber': fixorder,
            'dcUuid': '000002010000001'
        }
        url = 'http://app2.iwms.hd123.cn:8081/test/iwms-facility/facility/order/getByBillNumberOrSourceBillNumberAndDcUuid'
        headers = {'content-type': "application/json", 'check_flag': 'false'}
        response = requests.get(url,params=data,headers=headers)
        print(response.status_code)
        order_result = response.json()
        print (order_result)
        assert response.status_code == 200
        data2 = {
            'uuid':order_result['data']['uuid'],
            'version':order_result['data']['version'],
        }
        print(data2)
        url = 'http://app2.iwms.hd123.cn:8081/test/iwms-facility/facility/order/abort/%s' %data2['uuid']+'?version=%s' %data2['version']
        headers = {'content-type': "application/json", 'check_flag': 'false'}
        response = requests.post(url,headers=headers)
        print(response.status_code)
        assert response.status_code == 200
        # print (response.text)
        r1 = response.json()
        print (r1)
        if r1['success'] == True:
            print('作废成功')
        else:
            print('作废失败','错误信息为:'+ r1['message'])


#
# if __name__ == '__main__':
#     pytest.main(['-s,--alluredir D:/Alice/jieguo'])
