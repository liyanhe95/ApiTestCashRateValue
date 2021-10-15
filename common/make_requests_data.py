import json
from common import logger
from common.replace_prarm import ReplaceParam
from common.read_excel import ReadExcel


logger = logger.get_logger("data")
class MakeRequestsData:
    def __init__(self,excel_case):
        self.case_titledata = ReadExcel(excel_case).read_excel()

    def make_requestsdata(self,request_json):
        '''
        将请求的json串中的参数进行替换，
        并将请求参数、用例id、用例名称、jsonpath路径、断言组装成字典放入列表中
        '''
        requests_list = []
        for i in self.case_titledata:
            '''获取请求的json串'''
            logger.info("id为 {}：".format(i["id"]))
            logger.info("casename为 {}：".format(i["casename"]))
            # request_dict = {}
            with open(request_json,'r',encoding='utf-8') as fp:
                self.requests_data = json.load(fp)
            logger.info("请求json打印" + str(self.requests_data))
            requests_json = self.requests_data
            '''将json串中的参数进行替换'''
            ReplaceParam().replace_param(requests_json, i)
            i["requests_data"]= requests_json
            requests_list.append(i)
            if isinstance(i["assert_value2"], float):
                i["assert_value2"] = str(i["assert_value2"])
            logger.info("assert_value2 {}：".format(i["assert_value2"]))
            logger.info("assert_value2 {}：".format(type(i["assert_value2"])))

        return requests_list




        # logger.info(self.requests_list)


if __name__ == '__main__':
   from common import contants
   MakeRequestsData(contants.case_zhengqingchun).make_requestsdata(contants.json_zhengqingchun)
