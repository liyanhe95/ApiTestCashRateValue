import requests
import json
from common import logger
from common.utils import get_token


logger = logger.get_logger("request")
class Request:
    # 定义一个requests类
    def __init__(self):

        read_token = get_token()
        self.search_header = {"Token":read_token,'Content-Type':'application/json','charset':'UTF-8'}
        # self.url =  "https://broker-gateway-sit.zhuanxinbaoxian.com/product/ratetrial/getTrialValue"



    def request(self,data):
        trial_url = "https://broker-gateway-sit.zhuanxinbaoxian.com/product/ratetrial/getTrialValue"
        trial_resp = requests.request('post',url=trial_url,json=data,headers = self.search_header)# 调用get方法，使用params传参（url传参）
        json_temp = json.loads(trial_resp.text)
        ratetrial_resp = json_temp['data']['rateTrialRespVO']['rateTrialReqVO']
        logger.info('response: {0}'.format(trial_resp.text))
        return ratetrial_resp

    def rate_request(self,ratetrial_resp):
        rate_url = "https://broker-gateway-sit.zhuanxinbaoxian.com/product/ratetrial/getCashRateValue"
        resp = requests.request('post', url=rate_url, json=ratetrial_resp, headers=self.search_header)
        logger.info('response: {0}'.format(resp))
        return resp





if __name__ == '__main__':
    import json
    data = {"productCode":"PL00025","planCode":"","preOrderNo":"","trialGenes":{}}
    request = Request().request(data)
    rate = Request().rate_request(request)
    # print(request.text)
    # json_temp = json.loads(request.text)
    # print(json_temp)
