import pytest
import requests
import json
from common.MysqlHelper import MysqlHelper

class Test_Article():
    def test_article(self):
        # companyUuid = '0000045'
        # dcUuid = '000004510000001'
        # 连接数据库
        helper = MysqlHelper('db2.iwms.hd123.cn', 3306, 'iwms', 'iwms', 'iwmsbasic')
        # 从数据库中取到想要的值
        varticleSql = "SELECT uuid, code, name FROM iwmsbasic.iwmsarticle  WHERE companyuuid='0000007' " \
                      "and ownercode='H001' and code like'%%A%%'ORDER BY uuid LIMIT " + str(2)
        articles = helper.get_all(varticleSql)
        for article in articles:
          data = {
            "article": {
                "code": article[1],
                "name": article[2],
                "uuid": article[0]
            },
            "caseBinCode": "",
            "companyUuid": "0000045",
            "dcUuid": "000004510000001",
            "splitBinCode": ""
        }
        url = 'http://app2.iwms.hd123.cn:8081/test/iwms-facility/facility/pickscheme'
        headers = {'content-type': 'application/json', 'check_flag': 'false'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        resp = response.json()
        print(resp)
        if response.status_code == 200:
            print('删除拣货位成功，拣货位code：')
        elif response.status_code == 500:
            print('删除拣货位失败，原因：' + resp['message'])
        else:
            print('检查数据正确性')
        assert response.status_code == 200
    #
if __name__ == '__main__':
    a = Test_Article()
    a.test_article()