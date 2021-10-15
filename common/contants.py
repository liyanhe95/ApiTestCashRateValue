#无论在哪用都可以直接contants.
import os
# 项目地址
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #项目根路径
# datas 目录地址
data_dir = os.path.join(base_dir,"datas")#拼接路径  找到data文件夹
# print(data_dir)

#log地址
log = os.path.join(base_dir,"log")
log_dir = os.path.join(log,"case.log")
# print(log_dir)

#get_user_token
use_file = os.path.join(data_dir,"login_token.text")
print(use_file)

#华贵
"""正青春试算用例路径"""
case_zhengqingchun = os.path.join(data_dir,"excel_case/company_huagui/正青春现价.xlsx")
# print("excel用例地址：",case_zhengqingchun)

"""正青春请求参数JSON："""
json_zhengqingchun = os.path.join(data_dir,"request_json/company_huagui/zhengqingchun_request.json")
# print("正青春请求参数JSON地址：",json_zhengqingchun)

#复星
case_kangleyisheng = os.path.join(data_dir,"excel_case/company_fuxing/康乐一生现价用例.xlsx")
# print("excel用例地址：",case_klys)
json_kangleyisheng = os.path.join(data_dir,"request_json/company_fuxing/kangleyisheng_request.json")
# print("正青春请求参数JSON地址：",json_klys)