import requests
import json
import pymysql

conn =pymysql.connect(host='db2.iwms.hd123.cn',user='iwms',passwd='iwms',db='iwmsfacility'
                      ,port=3306,charset='utf8')
cur =conn.cursor()

cur.execute("SELECT uuid,dcUuid,articleUuid,binCode FROM iwmsfacility.iwmshighlowstock WHERE "
            "highStockQtyStr = 0  and lowStockQtyStr = 0  LIMIT 3136")
kucun = cur.fetchall()
conn.commit()
conn.close()
print(kucun)

n = 0
while n < 3035:
    n = n + 1

    url = 'http://app2.iwms.hd123.cn:8081/test/iwms-facility/facility/highLowStock/modify?lang=zh_CN'
    headers = {'content-type': 'application/json', 'check_flag': 'false'}


    data = {
   "uuid": kucun[n-1][0],
   "dcUuid": kucun[n-1][1],
   "articleUuid": kucun[n-1][2],
   "binCode": kucun[n-1][3],
   "qpcStr": "1*1*1",
   "highStockQtyStr": 100,
   "lowStockQtyStr": 1
}
    print(data)

    r = requests.post(url, json.dumps(data), headers=headers)

    print('正常编辑库存的结果为：')
    print(r.json())