# coding=utf-8
import datetime
import time
import requests
import json
import decimal
import pytest
class Test_iwmsarticle():
    def test_iwmsarticle(self):
        n = 1
        while n < 10:
            code='H00'+str(n)
            name='商品'+str(n)
            n = n+1
            data={
                "code": code,
                "name": name,
                "shortName": "无",
                "owner": "{\"uuid\":\"0b9b9ffb1c29421ebafade7856c54e23\",\"code\":\"8888\",\"name\":\"默认货主\"}",
                "spec": "个",
                "category": "{\"uuid\":\"8320474f537340c688e266f1c33685fa\",\"code\":\"A001\",\"name\":\"商品类别1\"}",
                "barcode": "随机",
                "defaultVendor": "{\"uuid\":\"000005030000001\",\"code\":\"H001\",\"name\":\"1号供应商\",\"type\":\"VENDOR\"}",
                "purchasePrice": 3,
                "salePrice": 3,
                "origin": "java",
                "shelfLifeType": "VALIDDATE",
                "shelfLifeDays": 60,
                "receiveControlDays": 30,
                "deliveryControlDays": 30,
                "returnControlDays": 30,
                "note": "",
                "companyUuid": "0000050",
                "sourceWay": "CREATE",
                "categoryCode": "A002",
                "ownerCode": "8888",
                "defaultVendorCode": "H001"
                }
            url = "http://app2.iwms.hd123.cn:8081/test/iwms-basic/basic/article"
            headers = {'content-type': 'application/json', 'check_flag': 'false'}
            response = requests.post(url, data=json.dumps(data), headers=headers)
            req = response.json()
            print(req)
        if response.status_code == 200:
            print('新增商品成功，商品：' + code)
        elif response.status_code == 500:
            print('新增商品失败，原因：' + req['message'])
        else:
            print('检查数据正确性')
            assert response.status_code == 200

if __name__ == '__main__':
    a = Test_iwmsarticle()
    a.test_iwmsarticle()

