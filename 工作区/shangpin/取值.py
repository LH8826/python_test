import datetime
import time
import requests
import json
from common.MysqlHelper import *
import decimal
import pytest
class Test_Pickcheme():
    def test_pickchemes(self):
        #定义变量
        companyUuid = '0000045'
        dcUuid = '000004510000001'
        #连接数据库
        helper = MysqlHelper('db2.iwms.hd123.cn', 3306, 'iwms', 'iwms', 'iwmsbasic')
        #从数据库中取到想要的值
        varticleSql = "SELECT uuid, code, name FROM iwmsbasic.iwmsarticle x WHERE companyuuid='0000007' " \
                      "and ownercode='8888' and code like'%%A%%'ORDER BY x.uuid "
        articles = helper.get_all(varticleSql)
        #打印查看值是否想要值
        print(articles)
        #遍历数据并打印查看
        for article in articles:
            print(article)
        #取整件拣货位（拣货位）
        helper = MysqlHelper('db2.iwms.hd123.cn', 3306, 'iwms', 'iwms', 'iwmsfacility')
        casebincode ="SELECT DISTINCT b.code, b.binUsage FROM iwmsbin AS b  LEFT JOIN iwmspickscheme AS ps ON ((ps.caseBinCode = b.code) OR (ps.splitBinCode = b.code))  " \
                     " AND (ps.dcUuid = '000004510000001') AND (ps.companyUuid = '0000045') WHERE (b.dcUuid = '000004510000001')" \
                     " AND (b.companyUuid = '0000045') AND (((b.binUsage = 'PickUpBin') AND (b.state = 'FREE') " \
                     " AND (ps.caseBinCode IS NULL) AND (ps.splitBinCode IS NULL))) ORDER BY b.code ASC"
        casebincodes = helper.get_all(casebincode)
        print(casebincode)
    # 取整件拆零拣货位（拣货位）
    helper = MysqlHelper('db2.iwms.hd123.cn', 3306, 'iwms', 'iwms', 'iwmsfacility')
    splitbincode = "SELECT DISTINCT b.code, b.binUsage FROM iwmsbin AS b LEFT JOIN iwmspickscheme AS ps ON ((ps.caseBinCode = b.code) OR (ps.splitBinCode = b.code))  " \
           " AND (ps.dcUuid = '000004510000001') AND (ps.companyUuid = '0000045') WHERE (b.dcUuid = '000004510000001') AND (b.companyUuid = '0000045') " \
           " AND (((b.binUsage = 'PickUpBin') AND (b.state = 'FREE') " \
           " AND (ps.caseBinCode IS NULL) AND (ps.splitBinCode IS NULL))) ORDER BY b.code ASC LIMIT"
    splitbincodes=helper.get_all(splitbincode)
    print(splitbincodes)
    # 取整件(拣货位），拆零拣货位(拣货存储位）
    # 拣货存储位
    helper = MysqlHelper('db2.iwms.hd123.cn', 3306, 'iwms', 'iwms', 'iwmsfacility')
    v_split_sql = "SELECT DISTINCT b.code, b.binUsage FROM iwmsbin AS b LEFT JOIN iwmspickscheme AS ps ON ((ps.caseBinCode = b.code) OR (ps.splitBinCode = b.code)) " \
                  " AND (ps.dcUuid = '000004510000001') " \
                  " AND (ps.companyUuid = '0000045') WHERE (b.dcUuid = '000004510000001') AND (b.companyUuid = '0000045') AND (((b.binUsage = 'PickUpStorageBin') " \
                  " ND (b.state = 'FREE') AND (ps.caseBinCode IS NULL) AND (ps.splitBinCode IS NULL))) ORDER BY b.code ASC LIMIT "

    # 拣货位
    v_case_sql = "SELECT DISTINCT b.code, b.binUsage FROM iwmsbin AS b LEFT JOIN iwmspickscheme AS ps ON ((ps.caseBinCode = b.code) OR (ps.splitBinCode = b.code))  " \
                 " AND (ps.dcUuid = '000004510000001') AND (ps.companyUuid = '0000045') WHERE (b.dcUuid = '000004510000001')" \
                 " AND (b.companyUuid = '0000045') AND ((b.binUsage = 'PickUpStorageBin') OR ((b.binUsage = 'PickUpBin')AND (b.state = 'FREE') " \
                 " AND (ps.caseBinCode IS NULL) AND (ps.splitBinCode IS NULL))) ORDER BY b.code ASC LIMIT "
    split_bins = helper.get_all(v_split_sql)
    case_bins = helper.get_all(v_case_sql)
    print(split_bins)
    print(case_bins)

if __name__ == '__main__':
        a=Test_Pickcheme()
        a.test_pickchemes