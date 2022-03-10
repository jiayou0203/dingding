# -- coding: utf-8 --

import requests
from web.header_body import header_body
import json

s=requests.Session()

class  qingqiu:

    def  __init__(self):
        self.header= header_body().header()                   # 设置请求header
        self.body=header_body().bodylogindata()                # 设置请求body

    #登录并返回token
    def postlogin(self,url):
        self.url = url
        re=s.post(self.url,self.body,self.header)
        shuju = re.text  # 返回信息
        shuju = json.loads(shuju)
        return shuju["token"]                             #登陆成功token获取


    # 获取arkid所有用户流程
    def search_user(self,url,token):
        self.url=url
        del self.header['Content-Type']
        del self.header['Origin']
        del self.header['Content-Length']
        self.header['Authorization']="token"+" "+token
        self.header['Cookie'] = "spauthn="+token
        userinfor=[]
        search_re = s.get(self.url,headers=self.header)
        shuju = search_re.text
        shuju = json.loads(shuju)
        for i in range(len(shuju['results'])):
            userinfor.append(shuju['results'][i]['username'])
        return userinfor


    # 新增arkid用户流程
    def add_user(self, url, token,name,password):
        self.url = url
        self.header['Content-Length'] = '362'
        self.header['Authorization'] = "token" + " " + token
        self.header['Cookie'] = "spauthn=" + token
        payload = "{\"user\":{\"avatar\":\"\",\"email\":\"\",\"employee_number\":\"\",\"gender\":0,\"mobile\":\"\",\"name\":\""+name+"\",\"position\":\"\",\"private_email\":\"\",\"username\":\""+name+"\",\"custom_user\":{\"data\":{}},\"depts\":null,\"roles\":null,\"nodes\":[],\"is_settled\":false,\"password\":\""+password+"\",\"require_reset_password\":false,\"has_password\":true,\"is_extern_user\":false,\"hiredate\":null},\"node_uids\":[]}"
        self.body=payload
        re = requests.request("POST", url, data=self.body, headers=self.header)
        shuju = re.text  # 返回信息
        shuju = json.loads(shuju)
        return shuju

    def del_user(self,url,token,user):
        del self.header['Host']
        del self.header['Connection']
        del self.header['Content-Length']
        del self.header['Pragma']
        del self.header['Cache-Control']
        del self.header['Accept']
        del self.header['Content-Type']
        del self.header['Origin']
        del self.header['X-Requested-With']
        del self.header['User-Agent']
        del self.header['Referer']
        del self.header['Accept-Encoding']
        del self.header['Accept-Language']
        del self.header['Cookie']
        self.header['Authorization'] = "token" + " " + token
        self.url=url+user+"/"
        re = requests.request("DELETE", self.url,headers=self.header)
        return re.text


