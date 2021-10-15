class ReplaceParam:

    def replace_param(self,request_data,case_titledata):
        """将请求参数中的变量进行替换"""
        if isinstance(request_data, dict):
            for key, value in request_data.items():
                if "$" in str(value):
                    if isinstance(value,str):
                        # print("value is str",value)
                        request_data[key] = case_titledata[value[2:-1]]
                    else:
                        # print("value is not str", value)
                        self.replace_param(value,case_titledata)
        if isinstance(request_data,list):
            for i in request_data:
                if "$" in str(i):
                    if isinstance(i,dict):
                        # print("i is dict", i)
                        self.replace_param(i,case_titledata)
                    elif isinstance(i,list):
                        # print("i is list", i)
                        self.replace_param(i,case_titledata)
        return request_data






