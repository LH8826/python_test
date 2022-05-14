#coding=utf-8
import datetime
import time
import requests
import json
import decimal
import pytest
n = 1
while n <= 8:
    code = 'H600' + str(n)
    name = '苹果' + str(n)
    n = n + 1
    url="http://app2.iwms.hd123.cn:8081/test/iwms-basic/basic/article"
    headers = {'content-type': 'application/json', 'check_flag': 'false'}
    data1 = {
        "code": code,
        "name": name,
        "shortName": "无",
        "owner": "{\"uuid\":\"84840bc9ce604be4afbd12fe773a9437\",\"code\":\"H001\",\"name\":\"一号货主\"}",
        "spec": "个",
        "category": "{\"uuid\":\"efa1087e21cd4e23b12301b686c9d8a7\",\"code\":\"H002\",\"name\":\"糕点\"}",
        "barcode": "随机",
        "defaultVendor": "{\"uuid\":\"000000730000002\",\"code\":\"H002\",\"name\":\"供应商二号\",\"type\":\"VENDOR\"}",
        "purchasePrice": 3,
        "salePrice": 3,
        "origin": "java",
        "shelfLifeType": "VALIDDATE",
        "shelfLifeDays": 30,
        "receiveControlDays": 30,
        "deliveryControlDays": 30,
        "returnControlDays": 30,
        "note": "空",
        "companyUuid": "0000007",
        "sourceWay": "CREATE",
        "categoryCode": "H002",
        "ownerCode": "H001",
        "defaultVendorCode": "H002"
    }

    r1 = requests.post(url, json=data1, headers=headers)
    req = r1.json()
    print(r1.json())
    print(data1)
    if r1.status_code == 200:
        print('新增商品成功，商品uuid：' + req['data'])
    elif r1.status_code == 500:
        print('新增商品失败，原因：' + req['message'])
    else:
        print('检查数据正确性')
    assert r1.status_code == 200
