import datetime
import time
import requests
import json
from common.MysqlHelper import *
import decimal
import pytest
import allure
import copy

class TestClass_NewOrder():
    def test_neworder(self,fixorder):
        # 以下是新增订单
        # 定义传入参数
        # print(fixorder)
        tneworder = {
        'vcompanyUuid' : '0000020',
        'vdcUuid' : '000002010000001',
        'vexpireDate' : '2020-05-06 12:09:30',
        'vlogisticMode' : 'UNIFY',
        'vnote' : 'test订单',
        'vownercode' : '8888',
        'vownername' : '默认货主',
        'vowneruuid' : '8cc19f2a7bc54ea6b53e13de481b9588',
        'vsourceBillNumber' : fixorder,
        'vvendorcode' : 'Y001',
        'vvendorname' : 'Y001供应商',
        'vvendoruuid' : '000002030000001',
        'vwrhcode' : 'Y001',
        'vwrhname' : '01仓',
        'vwrhuuid' : '7c5cdc01ded348a8a81702e61ed03a6f',
        }
        tneworderitem ={
        'varticlecode1' : 'Y001',
        'varticlename1' : '香蕉',
        'varticleuuid1' : '4ce3437d8b0e4a5297100ddf9455259f',
        'varticleline1' : 1,
        'varticlemunit1' : '箱',
        'varticlenote1' : '货品1',
        'varticleprice1' : decimal.Decimal(10),
        'varticleqpcStr1' : "1*1*1",
        'varticleqtyStr1' : "0+3",
        'varticlecode2' : 'Y002',
        'varticlename2' : '苹果',
        'varticleuuid2' : '9d7241993a2844329762596deeea6511',
        'varticleline2' : 2,
        'varticlemunit2' : '箱',
        'varticlenote2' : '货品2',
        'varticleprice2' : decimal.Decimal(15),
        'varticleqpcStr2' : "1*2*3",
        'varticleqtyStr2' : "9+8",
        }

        #传入接口，创建定单
        url = 'http://app2.iwms.hd123.cn:8081/test/iwms-facility/facility/order'
        body = {
              "companyUuid": "%s" %tneworder['vcompanyUuid'],
              "dcUuid": "%s" %tneworder['vdcUuid'],
              "expireDate": "%s" %tneworder['vexpireDate'],
              "items": [
                {
                  "article": {
                    "code": "%s" %tneworderitem['varticlecode1'],
                    "name": "%s" %tneworderitem['varticlename1'],
                    "uuid": "%s" %tneworderitem['varticleuuid1']
                  },
                  "line": "%s" %tneworderitem['varticleline1'],
                  "munit": "%s" %tneworderitem['varticlemunit1'],
                  "note": "%s" %tneworderitem['varticlenote1'],
                  "price": "%s" %tneworderitem['varticleprice1'],
                  "qpcStr": "%s" %tneworderitem['varticleqpcStr1'],
                  "qtyStr": "%s" %tneworderitem['varticleqtyStr1']
                },
                {
                  "article": {
                    "code": "%s" %tneworderitem['varticlecode2'],
                    "name": "%s" %tneworderitem['varticlename2'],
                    "uuid": "%s" %tneworderitem['varticleuuid2']
                  },
                  "line": "%s" %tneworderitem['varticleline2'],
                  "munit": "%s" %tneworderitem['varticlemunit2'],
                  "note": "%s" %tneworderitem['varticlenote2'],
                  "price": "%s" %tneworderitem['varticleprice2'],
                  "qpcStr": "%s" %tneworderitem['varticleqpcStr2'],
                  "qtyStr": "%s" %tneworderitem['varticleqtyStr2']
                }
              ],
              "logisticMode": "%s" %tneworder['vlogisticMode'],
              "note": "%s" %tneworder['vnote'],
              "owner": {
                "code": "%s" %tneworder['vownercode'],
                "name": "%s" %tneworder['vownername'],
                "uuid": "%s" %tneworder['vowneruuid']
              },
              "sourceBillNumber": "%s"  %tneworder['vsourceBillNumber'],
              "sourceWay": "CREATE",
              "vendor": {
                "code": "%s" %tneworder['vvendorcode'],
                "name": "%s" %tneworder['vvendorname'],
                "uuid": "%s" %tneworder['vvendoruuid']
              },
              "wrh": {
                "code": "%s" %tneworder['vwrhcode'],
                "name": "%s" %tneworder['vwrhname'],
                "uuid": "%s" %tneworder['vwrhuuid']
              }
            }
        headers = {'content-type': "application/json", 'check_flag': 'false'}
        response = requests.post(url, data=json.dumps(body), headers=headers)
        print(response.status_code)
        assert response.status_code == 200
        # print (response.text)
        r1 = response.json()
        print (r1)
        r3 = r1['success']
        if r3 == True:
            r2 = r1['data']
            print('添加成功','定单uuid为'+ r2)
        else:
            print('添加失败','错误信息为:'+ r1['message'])
        # r1 ={'data': '78b5575a8a0c4132a6a010c672298a74', 'success': True}
        # r2 = r1['data']

        # 查询数据库，核对传入数据
        helper = MysqlHelper('db2.iwms.hd123.cn', 3306, 'iwms', 'iwms', 'iwmsfacility')
        # 执行sql语句
        sqlmst = "select billNumber,companyUuid,dcUuid,expireDate,logisticMode,note," \
              "ownerCode,ownerName,ownerUuid,sourceBillNumber,vendorCode,vendorName,vendorUuid," \
              "wrhCode,wrhName,wrhUuid " \
              "from iwmsorderbill where Uuid = '%s'" %r2
        # print(sqlmst)
        ordermst = helper.get_all(sqlmst)  # 执行sql语句，返回sql查询成功的记录数目
        # print(ordermst)
        # vBillNumber = ordermst[0][0]

        sqlitem = "select articleCode,articleName,articleUuid,line,munit,note,price," \
                  "qpcStr,qtyStr from iwmsorderbillitem " \
                  "where Billuuid = '%s' order by line" %r2
        # print(sqlitem)
        orderitem = helper.get_all(sqlitem)  # 执行sql语句，返回sql查询成功的记录数目
        # print(orderitem,type(orderitem))

        #核对数据库和字典传入参数
        #转换汇总表日期
        d1 = tneworder['vexpireDate'].split(' ')[0]
        d2 = datetime.datetime.strptime(d1, '%Y-%m-%d').date()
        d3 = {'vexpireDate':d2}
        tneworder_check = tneworder.copy()
        tneworder_check.update(d3)
        ordermstlist_expresult = list(tneworder_check.values())
        ordermstlist_actresult = list(ordermst[0])
        ordermstlist_actresult.pop(0)
        # 转换第一个商品
        if "+" in tneworderitem['varticleqtyStr1']:
            m01 = int(tneworderitem['varticleqtyStr1'].split('+')[0])
            m02 = int(tneworderitem['varticleqtyStr1'].split('+')[-1])
        else:
            m01 = int(tneworderitem['varticleqtyStr1'])
            m02 = 0
        b02 = tneworderitem['varticleqpcStr1'].split('*', 2)
        n01 = int(b02[0])
        n02 = int(b02[1])
        if len(b02) == 2:
            n03 = 1
        else:
            n03 = int(b02[2])
        p01 = list(divmod(m01 * n01 * n02 * n03 + m02, n01 * n02 * n03))
        # print(p01, type(p01))
        if p01[1] == 0:
            s01 = str(p01[0])
        else:
            s01 = str(p01[0]) + '+' + str(p01[1])
        #转换第二个商品
        if "+" in tneworderitem['varticleqtyStr2']:
            m11 = int(tneworderitem['varticleqtyStr2'].split('+')[0])
            m12 = int(tneworderitem['varticleqtyStr2'].split('+')[-1])
        else:
            m11 = int(tneworderitem['varticleqtyStr2'])
            m12 = 0
        b12 = tneworderitem['varticleqpcStr2'].split('*', 2)
        n11 = int(b12[0])
        n12 = int(b12[1])
        if len(b12) == 2:
            n13 = 1
        else:
            n13 = int(b12[2])
        p11 = list(divmod(m11 * n11 * n12 * n13 + m12, n11 * n12 * n13))
        # print(p11, type(p11))
        if p11[1] == 0:
            s11 = str(p11[0])
        else:
            s11 = str(p11[0]) + '+' + str(p11[1])
        tneworderitem_check = tneworderitem.copy()
        tneworderitem_check.update({'varticleqtyStr1': s01})
        tneworderitem_check.update({'varticleqtyStr2': s11})
        orderitemlist_expresult = list(tneworderitem_check.values())
        orderitemlist_actresult = list(orderitem[0])
        orderitemlist_actresult.extend(list(orderitem[1]))

        print(ordermstlist_expresult, type(ordermstlist_expresult))
        print(ordermstlist_actresult, type(ordermstlist_actresult))
        print(orderitemlist_expresult, type(orderitemlist_expresult))
        print(orderitemlist_actresult, type(orderitemlist_actresult))
        #断言两者是否相等
        assert ordermstlist_expresult == ordermstlist_actresult
        assert orderitemlist_expresult == orderitemlist_actresult


if __name__ == '__main__':
    # a = TestClass_neworder()
    # a.test_neworder()
    pytest.main(['-s','-q','D:/pycharm/test/hdiwms/test_order/test_1_neworder.py',
                 '--alluredir', 'D:/Alice/jieguo',])
