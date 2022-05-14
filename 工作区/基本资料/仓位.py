# coding=utf-8
import datetime
import time
import requests
import json
import decimal
import pytest
class Test_iwmsarh():
    def test_iwmsarh(self):
        n = 1
        while n < 10:
            code='H00'+str(n)
            name='仓位'+str(n)
            n = n+1
            data={
                  "code": code,
                  "companyUuid": "0000050",
                  "dc": "000005010000001",
                  "name": name,
                  "note": "",
                  "sourceWay": "CREATE",
                  "sourceWrhCode": "",
                  "sourceWrhName": "",
                  "state": "ONLINE"
                }
            url = "http://app2.iwms.hd123.cn:8081/test/iwms-basic/basic/wrh"
            headers = {'content-type': 'application/json', 'check_flag': 'false'}
            response = requests.post(url, data=json.dumps(data), headers=headers)
            req = response.json()
            print(req)
        if response.status_code == 200:
            print('新增仓位成功，仓位：' + code)
        elif response.status_code == 500:
            print('新增仓位失败，原因：' + req['message'])
        else:
            print('检查数据正确性')
            assert response.status_code == 200

if __name__ == '__main__':
    a = Test_iwmsarh()
    a.test_iwmsarh()

