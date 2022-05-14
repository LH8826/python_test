import requests
import json
from 工作区.商品固定拣货分区业务.MysqlHelper import MysqlHelper

class TestClass_pickscheme():
    def test_picksch(self):
        company_uuid = '0000045'
        dc_uuid = '000004510000001'
        helper = MysqlHelper('db2.iwms.hd123.cn', 3306, 'iwms', 'iwms', 'iwmsbasic')
        v_article_sql = "SELECT uuid, code, name FROM iwmsbasic.iwmsarticle x WHERE companyuuid='0000045' " \
                        " and ownercode='8888' and code like'%%A%%'ORDER BY x.code LIMIT "+str(2000)
        articles = helper.get_all(v_article_sql)
        print(articles)
        article_len = len(articles)

        """
        前500商品 整件拣货位[拣货位]
        500 - 1500 整件拣货位[拣货位] 和 拆零拣货位[拣货存储位]
        1500 - 2000 拆零拣货位
        """
        if article_len > 1500:
            save_case_pick_bin(articles[:500], company_uuid, dc_uuid)
            save_pickstoragein_or_pickbin(articles[500:1500], company_uuid, dc_uuid)
            save_split_pick_bin(articles[1500:], company_uuid, dc_uuid)
        elif 501 < article_len <= 1500:
            save_case_pick_bin(articles[:500], company_uuid, dc_uuid)
            save_pickstoragein_or_pickbin(articles[500:article_len], company_uuid, dc_uuid)
        else:
            save_case_pick_bin(articles, company_uuid, dc_uuid)


def save_case_pick_bin(articles, company_uuid, dc_uuid):
    """
    保存整件拣货位[拣货位]
    :param dc_uuid: 配送中心uuid
    :param company_uuid: 企业uuid
    :param articles: 商品信息
    :return: None
    """
    helper = MysqlHelper('db2.iwms.hd123.cn', 3306, 'iwms', 'iwms', 'iwmsfacility')

    # 整件拣货位(货位筛选）
    vsql = "SELECT DISTINCT b.code, b.binUsage FROM iwmsbin AS b " \
           " LEFT JOIN iwmspickscheme AS ps ON ((ps.caseBinCode = b.code) OR (ps.splitBinCode = b.code)) " \
           " AND (ps.dcUuid = '000004510000001') AND (ps.companyUuid = '0000045') WHERE (b.dcUuid = '000004510000001') " \
           " AND (b.companyUuid = '0000045') AND (((b.binUsage = 'PickUpBin') AND (b.state = 'FREE') " \
           " AND (ps.caseBinCode IS NULL) AND (ps.splitBinCode IS NULL))) and code between '05010111' and '0505999' ORDER BY b.code ASC LIMIT " + str(len(articles))

    bins = helper.get_all(vsql)

    for i, article in enumerate(articles):
        save_pick_scheme(article, bins[i][0], '', company_uuid, dc_uuid)


def save_split_pick_bin(articles, company_uuid, dc_uuid):
    """
    保存拆零拣货位[拣货位]
    :param dc_uuid: 配送中心uuid
    :param company_uuid: 企业uuid
    :param articles: 商品信息
    :return: None
    """
    helper = MysqlHelper('db2.iwms.hd123.cn', 3306, 'iwms', 'iwms', 'iwmsfacility')

    # 拆零拣货位
    vsql = "SELECT DISTINCT b.code, b.binUsage FROM iwmsbin AS b " \
           " LEFT JOIN iwmspickscheme AS ps ON ((ps.caseBinCode = b.code) OR (ps.splitBinCode = b.code)) " \
           " AND (ps.dcUuid = '000004510000001') AND (ps.companyUuid = '0000045') WHERE (b.dcUuid = '000004510000001') " \
           " AND (b.companyUuid = '0000045') AND (((b.binUsage = 'PickUpBin') AND (b.state = 'FREE') " \
           " AND (ps.caseBinCode IS NULL) AND (ps.splitBinCode IS NULL)))and code between '05060111' and '0506999' ORDER BY b.code ASC LIMIT " + str(len(articles))

    bins = helper.get_all(vsql)
    for i, article in enumerate(articles):
        save_pick_scheme(article, '', bins[i][0], company_uuid, dc_uuid)


def save_pickstoragein_or_pickbin(articles, company_uuid, dc_uuid):
    """
    保存整件拣货位（拣货位）和拆零拣货位（拣货存储位）
    :param dc_uuid: 配送中心uuid
    :param company_uuid: 企业uuid
    :param articles: 商品信息
    :return: None
    """
    helper = MysqlHelper('db2.iwms.hd123.cn', 3306, 'iwms', 'iwms', 'iwmsfacility')

    # 拣货存储位
    v_split_sql = "SELECT DISTINCT b.code FROM iwmsbin AS b " \
                  " LEFT JOIN iwmspickscheme AS ps ON ((ps.caseBinCode = b.code) OR (ps.splitBinCode = b.code)) " \
                  " AND (ps.dcUuid = '000004510000001') AND (ps.companyUuid = '0000045') WHERE (b.dcUuid = '000004510000001') " \
                  " AND (b.companyUuid = '0000045') AND (b.binUsage = 'PickUpStorageBin') and code between '05010111' and '0505999'ORDER BY b.code ASC LIMIT " + str(len(articles))

    # 拣货位
    v_case_sql = "SELECT DISTINCT b.code, b.binUsage FROM iwmsbin AS b " \
           " LEFT JOIN iwmspickscheme AS ps ON ((ps.caseBinCode = b.code) OR (ps.splitBinCode = b.code)) " \
           " AND (ps.dcUuid = '000004510000001') AND (ps.companyUuid = '0000045') WHERE (b.dcUuid = '000004510000001') " \
           " AND (b.companyUuid = '0000045') AND (((b.binUsage = 'PickUpBin') AND (b.state = 'FREE') " \
           " AND (ps.caseBinCode IS NULL) AND (ps.splitBinCode IS NULL)))and code between '05010111' and '0505999' ORDER BY b.code ASC LIMIT " + str(len(articles))

    split_bins = helper.get_all(v_split_sql)
    case_bins = helper.get_all(v_case_sql)

    for i, article in enumerate(articles):
        save_pick_scheme(article, case_bins[i][0], split_bins[i][0], company_uuid, dc_uuid)


def save_pick_scheme(article, case_bin_code, split_bin_code, company_uuid, dc_uuid):
    """
    保存拣货方案
    :param article: 商品
    :param case_bin_code: 整件拣货位
    :param split_bin_code: 拆零拣货位
    :param company_uuid: 企业uuid
    :param dc_uuid: 配送中uuid
    :return: None
    """
    data = {
        "article": {
            "uuid": article[0],
            "code": article[1],
            "name": article[2]
        },
        "caseBinCode": case_bin_code,
        "companyUuid": company_uuid,
        "dcUuid": dc_uuid,
        "splitBinCode": split_bin_code
    }
    url = 'http://app2.iwms.hd123.cn:8081/test/iwms-facility/facility/pickscheme'
    headers = {'content-type': "application/json", 'check_flag': 'false'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    resp = response.json()

    if response.status_code == 200:
        print('操作商品成功, 商品代码：%s, 整件拣货位：%s，拆零拣货位：%s' % (article[1], case_bin_code, split_bin_code))
    elif response.status_code == 500:
        print('操作商品成功, 商品代码：%s, 整件拣货位：%s，拆零拣货位：%s, 失败原因：%s'
              % (article[1], case_bin_code, split_bin_code, resp['message']))
    else:
        print('检查数据正确性')
        assert response.status_code == 200


if __name__ == '__main__':
    a = TestClass_pickscheme()
    a.test_picksch()
