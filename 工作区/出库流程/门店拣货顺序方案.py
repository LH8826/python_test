import requests
import json
import pymysql

conn =pymysql.connect(host='db2.iwms.hd123.cn',user='iwms',passwd='iwms',db='iwmsfacility',port=3306,charset='utf8')
cur =conn.cursor()
cur.execute("select code,name,uuid from iwmsbasic.iwmsstore where code like '%D%' and companyuuid='0000036' and "
            "ownercode='hz01' ORDER BY code LIMIT 100")
mendian = cur.fetchall()
conn.commit()
conn.close()
print(mendian)
n = 0
while n < 100:
    n = n + 1
    url = 'http://app2.iwms.hd123.cn:8081/test/iwms-facility/facility/storepickorder/b16032daf66146cbb6fb29e18ca5912d/store?lang=zh_CN'
    headers = {'content-type': 'application/json', 'check_flag': 'false'}
    data = [
        {
         "uuid": mendian[n-1][2],
         "code": mendian[n-1][0],
         "name": mendian[n-1][1]
        }
    ]
    print(data)
    r = requests.post(url, json.dumps(data), headers=headers)
    print('正常新增门店的结果为：')
