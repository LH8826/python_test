# coding:utf-8

import datetime
import time
import requests
import json
from common.MysqlHelper import *
import decimal
import pytest

data = {
    "page": 0,
    "pageSize": 2,
    "searchKeyValues": {
        "companyUuid": "0000045",
        "dcUuid": "000004510000001"
    }
}

url = 'http://app2.iwms.hd123.cn:8081/test/iwms-facility/facility/bin/list/forArticleBusiness'
headers = {'content-type': "application/json", 'check_flag': 'false'}
response = requests.post(url, data=json.dumps(data), headers=headers)
resp = response.json()

print(resp)
print(resp['data'])

resdata = resp['data']

result = []
for item in resdata:
    result.append('code')
