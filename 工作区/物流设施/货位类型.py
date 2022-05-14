# coding=utf-8
import datetime
import time
import requests
import json
import decimal
import pytest
class Test_iwmsbintype():
    def test_iwmsbintype(self):
        n = 1
        while n < 10:
            code='H00'+str(n)
            name='货位类型'+str(n)
            n = n+1
            data={
                      "code": code,
                      "companyUuid": "0000050",
                      "dcUuid": "000005010000001",
                      "height": 100,
                      "length": 100,
                      "name": name,
                      "note": "",
                      "plotRatio": 100,
                      "storageNumber": 100,
                      "weight": 100,
                      "width": 100
                }
            url = "http://app2.iwms.hd123.cn:8081/test/iwms-facility/facility/bintype"
            headers = {'content-type': 'application/json', 'check_flag': 'false'}
            response = requests.post(url, data=json.dumps(data), headers=headers)
            req = response.json()
            print(req)
        if response.status_code == 200:
            print('新增货位类型成功，货位：' + code)
        elif response.status_code == 500:
            print('新增货位失败，原因：' + req['message'])
        else:
            print('检查数据正确性')
        assert response.status_code == 200

if __name__ == '__main__':
    a = Test_iwmsbintype()
    a.test_iwmsbintype()

