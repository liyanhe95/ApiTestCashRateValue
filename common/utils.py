import datetime
import requests
from common import contants
import json
import jsonpath

#
# a = 'year=-18&day='
# b = 'year=-41&day=1'
# years_delta_str, days_delta_str = b.replace('year=', '').replace('day=', '').split('&')
# if years_delta_str == '':
#     years_delta = 0
# else:
#     years_delta = int(years_delta_str)
# if days_delta_str == '':
#     days_delta = 0
# else:
#     days_delta = int(days_delta_str)
#
# now_time = datetime.datetime.now() # 获取当前时间
# now_str = now_time.strftime("%Y-%m-%d %H:%M:%S")  #当前时间转化成datetime标准格式
# now_year = int(now_str.split('-')[0]) + years_delta
# temp_time = datetime.datetime.strptime(str(now_year) + now_str[4:], "%Y-%m-%d %H:%M:%S")
# delta = datetime.timedelta(days=days_delta)
# result_time = temp_time + delta
# final_result = result_time.strftime("%Y-%m-%d %H:%M:%S").split(' ')[0]


def date_format(data_time):
    years_delta_str, days_delta_str = data_time.replace('year=', '').replace('day=', '').split('&')
    if years_delta_str == '':
        years_delta = 0
    else:
        years_delta = int(years_delta_str)
    if days_delta_str == '':
        days_delta = 0
    else:
        days_delta = int(days_delta_str)

    now_time = datetime.datetime.now()
    now_str = now_time.strftime("%Y-%m-%d %H:%M:%S")
    now_year = int(now_str.split('-')[0]) + years_delta
    temp_time = datetime.datetime.strptime(str(now_year) + now_str[4:], "%Y-%m-%d %H:%M:%S")
    delta = datetime.timedelta(days=days_delta)
    result_time = temp_time + delta
    final_result = result_time.strftime("%Y-%m-%d %H:%M:%S").split(' ')[0]
    return final_result

def get_token():
    url = "https://broker-gateway-sit.zhuanxinbaoxian.com/base/authorization/getTouristToken?channel=slb&dosage=null"
    request_result =  requests.request('get',url=url)
    gain_token = eval(request_result.text)['data']

    with open(contants.use_file, "w") as w:
        w.write(str(gain_token))
    with open(contants.use_file, "r") as r:
        read_token = r.read()
        return read_token


def postprogressing(resp, item):
    json_temp = json.loads(resp.text)
    cash_resp = jsonpath.jsonpath(json_temp, str(item['getResponseValue2']))
    total_cash = jsonpath.jsonpath(json_temp, str(item['getResponseValue1']))

    if isinstance(cash_resp, list) and len(cash_resp) == 1:
        cash_resp = cash_resp[0]
    if isinstance(cash_resp, float):
        cash_resp = str(cash_resp)

    try:
        '''将返回结果和期望结果进行匹配'''
        assert (cash_resp == item['assert_value2'] and total_cash == item['assert_value1'])
        print("第{}用例执行结果：PASS".format(item['id']))
    except AssertionError as e:
        print("第{}用例执行结果：FAIL".format(item['id']))
        raise e


if __name__ == '__main__':
    # date= date_format('year=-18&day=')
    # print(date)
    get_token()
