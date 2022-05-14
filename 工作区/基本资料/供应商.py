# coding=utf-8
import datetime
import time
import requests
import json
import decimal
import pytest
class Test_iwmsvendor():
    def test_iwmsvendor(self):
        n = 1
        while n < 10:
            code='H00'+str(n)
            name=str(n)+'号供应商'
            n = n+1
            data={
                    "address": {
                        "city": "昆明市",
                        "country": "中国",
                        "district": "西山区",
                        "province": "云南省",
                        "street": "西村街道"
                    },
                    "code": code,
                    "companyUuid": "0000050",
                    "contactPhone": "17894562133",
                    "contactor": "刘萌萌",
                    "homePage": "",
                    "name": name,
                    "note": "",
                    "ownerCode": "8888",
                    "shortName": name,
                    "sourceCode": "H001",
                    "sourceWay": "CREATE",
                    "state": "ONLINE",
                    "zipCode": ""
                }
            url = "http://app2.iwms.hd123.cn:8081/test/iwms-basic/basic/vendor"
            headers = {'content-type': 'application/json', 'check_flag': 'false'}
            response = requests.post(url, data=json.dumps(data), headers=headers)
            req = response.json()
            print(req)
        if response.status_code == 200:
            print('新增供应商成功，供应商uuid：' + req['data'])
        elif response.status_code == 500:
            print('新增供应商失败，原因：' + req['message'])
        else:
            print('检查数据正确性')
        assert response.status_code == 200

if __name__ == '__main__':
    a = Test_iwmsvendor()
    a.test_iwmsvendor()

