# -- coding: utf-8 --
# -- coding: utf-8 --
import requests
import json

appkey=" "
appsecret=" "

api_url = "https://oapi.dingtalk.com/gettoken?appkey=%s&appsecret=%s"%(appkey,appsecret)


def departList():
    # 所有部门信息
    url='https://oapi.dingtalk.com/user/listbypage?access_token={}&lang=zh_CN&department_id=560542547&offset=1&size=100&order=entry_asc'.format(get_token())#获取部门人员详情
#    url='https://oapi.dingtalk.com/department/get?access_token={}&id=560542547&lang=zh_CN'.format(get_token())    #获取部门详情
#    url='https://oapi.dingtalk.com/topapi/v2/user/getuserinfo?access_token={}'.format(get_token())
#    url="https://oapi.dingtalk.com/department/list?access_token={}&lang=zh_CN&fetch_child=true&id=479506421".format(get_token())
    print(url)
    ret = json.loads(requests.get(url).text)
    for i in range(0,len(ret['userlist'])):
        print(ret['userlist'][i])
    '''
    department = ret.get('department')
    print(department)
    departList = []
    for department_info in department:
        departdict = {}
        departdict['name'] = department_info.get('name')
        departdict['id'] = department_info.get('id')
        departdict['parentid'] = department_info.get('parentid')
        departList.append(departdict)
    return departList
    '''

def get_token():
    # try:
    res = requests.get(api_url)
    if res.status_code == 200:
        str_res = res.text
        token = (json.loads(str_res)).get('access_token')
        print("123")
        print(token)
        return token


if __name__ == '__main__':
    departList()