import pytest
from common import contants
from common.request import Request
from common import logger
from common.make_requests_data import MakeRequestsData
from common.utils import postprogressing
import json
import jsonpath

logger = logger.get_logger("kangleyisheng")#获取logger实例

class TestTrial():

    cases = MakeRequestsData(contants.case_kangleyisheng).make_requestsdata(contants.json_kangleyisheng)
    request = Request()

    def setUp(self):
        logger.info('开始执行康乐一生现价脚本')

    ids =  [case['casename'] for case in cases] # testData 为参数列表
    @pytest.mark.parametrize('item',cases,ids=ids)
    def test_huagui_zhengqingchun_cash(self,item):  #用一个变量来解释data传递的数据
        item['id'] = int(item['id'])
        logger.info("开始执行第{}用例".format(item['id']))
        # 使用封装好的request 来完成请求
        trial_resp = self.request.request(item['requests_data'])
        resp = self.request.rate_request(trial_resp)
        postprogressing(resp,item)


    def tearDown(self):
        logger.info('康乐一生现价脚本执行结束')
#
#
# if __name__ == '__main__':
#     pytest.main(' --pytest-tmreport-name=reports/report.html')
#     '''命令行用法：pytest --pytest-tmreport-name=reports/report.html'''
#     '''cmd执行pytest用例有三种方法,以下三种方法都可以，一般推荐第一个
#     pytest
#     py.test
#     python -m pytest'''
#

