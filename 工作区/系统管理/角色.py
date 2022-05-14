#coding=utf-8
import datetime
import time
import requests
import json
import decimal
import pytest
class Test_iwmssole():
   def test_iwmssole(self):
    data={
             "code": "0001",
             "companyUuid": "0000050",
             "name": "企业管理员",
             "note": "",
             "orgUuid": "0000050"
    }

    url = "http://app2.iwms.hd123.cn:8081/test/iwms-account/account/role"
    headers = {'content-type': 'application/json', 'check_flag': 'false'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    req = response.json()
    print(req)
    if response.status_code == 200:
        print('新增角色成功，角色uuid：' + req['data'])
    elif response.status_code == 500:
        print('新增角色失败，原因：' + req['message'])
    else:
        print('检查数据正确性')
    assert response.status_code == 200
if __name__ == '__main__':
    a = Test_iwmssole()
    a.test_iwmssole()
