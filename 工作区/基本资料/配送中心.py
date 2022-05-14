# coding=utf-8
import datetime
import time
import requests
import json
import decimal
import pytest


class Test_iwmsdc():
    def test_iwmsdc(self):
        n = 1
        while n < 10:
            code = 'A00' + str(n)
            name = str(n) + '号配送中心'
            n = n + 1
            data = {
                "address": {
                    "city": "昆明市",
                    "country": "中国",
                    "district": "西山区",
                    "province": "云南省",
                    "street": "西村街道"
                },
                "code": code,
                "companyUuid": "0000050",
                "contactPhone": "17687845357",
                "contactor": " 刘萌萌",
                "createInfo": {
                    "operator": {
                        "fullName": "灰灰",
                        "id": "00000500000001",
                        "namespace": "0000050",
                        "qualifiedId": "00000500000001@@0000050"
                    },
                    "time": "2019-07-21 00:00:00"
                },
                "homeUrl": "",
                "lastModifyInfo": {
                    "operator": {
                        "fullName": "灰灰",
                        "id": "00000500000001",
                        "namespace": "0000050",
                        "qualifiedId": "00000500000001@@0000050"
                    },
                    "time": "2019-07-21 00:00:00"
                },
                "name": name,
                "note": "",
                "operatingArea": 0,
                "shortName": name,
                "sourceCode": "string",
                "sourceWay": "CREATE",
                "state": "ONLINE",
                "useWMS": True,
                "uuid": "000005010000001",
                "version": 0,
                "versionTime": "2019-08-04 00:00:00",
                "zipCode": ""
                }
            url = "http://app2.iwms.hd123.cn:8081/test/iwms-basic/basic/dc"
            headers = {'content-type': 'application/json', 'check_flag': 'false'}
            response = requests.post(url, data=json.dumps(data), headers=headers)
            req = response.json()
            print(req)
        # if response.status_code == 200:
        #     print('新增配送中心成功，配送中心uuid：' + req['data'])
        # elif response.status_code == 500:
        #     print('新增配送中心失败，原因：' + req['message'])
        # else:
        #     print('检查数据正确性')
        # assert response.status_code == 200
if __name__ == '__main__':
    a = Test_iwmsdc()
    a.test_iwmsdc()
