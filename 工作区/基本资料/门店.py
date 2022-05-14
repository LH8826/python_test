# coding=utf-8
import datetime
import time
import requests
import json
import decimal
import pytest
class Test_iwmsowner():
    def test_iwmsowner(self):
        n = 1
        while n < 10:
            code='H00'+str(n)
            name='门店'+str(n)
            n = n+1
            data={
                "address": {
                    "city": "上海市",
                    "country": "中国",
                    "district": "闵行区",
                    "province": "上海市",
                    "street": "浦江镇"
                },
                "code": code,
                "companyUuid": "0000050",
                "contactPhone": "13689567850",
                "contactor": "企业",
                "distance": 0,
                "homeUrl": "",
                "name": code,
                "note": "",
                "operatingArea": 0,
                "operatingType": "连锁经营",
                "ownerCode": "8888",
                "shortName": "",
                "sourceUuid": "",
                "sourceWay": "CREATE",
                "storeType": "超市",
                "zipCode": ""
                }
            url = "http://app2.iwms.hd123.cn:8081/test/iwms-basic/basic/store"
            headers = {'content-type': 'application/json', 'check_flag': 'false'}
            response = requests.post(url, data=json.dumps(data), headers=headers)
            req = response.json()
            print(req)
        if response.status_code == 200:
            print('新增门店成功，门店uuid：' + req['data'])
        elif response.status_code == 500:
            print('新增门店失败，原因：' + req['message'])
        else:
            print('检查数据正确性')
            assert response.status_code == 200

if __name__ == '__main__':
    a = Test_iwmsowner()
    a.test_iwmsowner()

