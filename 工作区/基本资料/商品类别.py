# coding=utf-8
import  requests
import json
class Test_Category():
    def test_category(self):
        n = 0
        while n < 10:
            n = n + 1
            code = 'A00' + str(n)
            name = '商品类别' + str(n)
            data = {
                    "code": code,
                    "companyUuid": "0000050",
                    "level": "一级",
                    "name": name,
                    "note": "",
                    "ownerCode": "8888",
                    "sourceWay": "CREATE",
                    "state": "ONLINE",
                    "upperCode": ""
            }
            url = "http://app2.iwms.hd123.cn:8081/test/iwms-basic/basic/category/save"
            headers = {'content-type': 'application/json', 'check_flag': 'false'}
            response = requests.post(url, data=json.dumps(data), headers=headers)
            req = response.json()
            print(req)
        if response.status_code == 200:
            print('新增商品类别成功，商品类别code：' + code)
        elif response.status_code == 500:
            print('新增商品类别失败，原因：' + req['message'])
        else:
            print('检查数据正确性')
        assert response.status_code == 200
        if __name__ == '__main__':
            a = Test_Category()
            a.test_category()