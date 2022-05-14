import requests
import json
import pymysql

conn =pymysql.connect(host='db2.iwms.hd123.cn',user='iwms',passwd='iwms',db='iwmsfacility',port=3306,charset='utf8')
cur =conn.cursor()
cur.execute("select code,name,uuid from iwmsbasic.iwmsstore where code like '%S%' and companyuuid='0000045' and "
            "ownercode='8888' ORDER BY code LIMIT 2000")
mendian = cur.fetchall()
conn.commit()
conn.close()
n = 0
while n < 2000:
    n = n + 1
    url = 'http://app2.iwms.hd123.cn:8081/test/iwms-facility/facility/deliverycycle/0f2a40a143be4aeebc525406bfe2a46e/storeDeliveryCycle'
    headers = {'content-type': 'application/json', 'check_flag': 'false'}
    data = {
            "companyUuid": "0000045",
            "dcUuid": "000004510000001",
            "fri": "",
            "mon": "波次1",
            "sat": "",
            "store": {
                "uuid": mendian[n-1][2],
                 "code": mendian[n-1][0],
                 "name": mendian[n-1][1]
            },
            "storeGroup": {
                "code": "0001",
                "name": "01组",
                "uuid": "b7c3f60df0fa4c01af223e2a8ad0575c"
            },
            "sun": "",
            "thur": "波次1",
            "tues": "",
            "wed": ""
        }

    print(data)
    r = requests.post(url, json.dumps(data), headers=headers)
    print('正常新增门店的结果为：')
