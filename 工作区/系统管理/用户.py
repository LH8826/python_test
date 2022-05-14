# coding=utf-8
import datetime
import time
import requests
import json
import decimal
import pytest
class Test_iwmsuser():
    def test_iwmsuser(self):
        n = 1
        while n < 10:
            n = n + 1
            code = 'A00' + str(n)
            name = '用户' + str(n)
            phone = '1780259770' + str(n)

            companyuuid = '0000050'
            body = {
                "avatar": "string",
                "code": code,
                "companyUuid": companyuuid,
                "name": name,
                "orgUuids": [
                    "0000050"
                ],
                "phone": phone,
                "resources": [
                    "string"
                ],
                "roleUuids": [
                    "3491c63f6bef41e0835d94c3dde7ef76"
                ]
            }
            url = "http://app2.iwms.hd123.cn:8081/test/iwms-account/account/user"
            headers = {'content-type': 'application/json', 'check_flag': 'false'}
            response = requests.post(url, data=json.dumps(body), headers=headers)
            req = response.json()
            print(req)
        if response.status_code == 200:
            print('新增用户成功，用户uuid：' + req['data'])
        elif response.status_code == 500:
            print('新增用户失败，原因：' + req['message'])
        else:
            print('检查数据正确性')
            assert response.status_code == 200
if __name__ == '__main__':
    a = Test_iwmsuser()
    a.test_iwmsuser()

