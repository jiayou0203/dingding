# -- coding: utf-8 --



import json
from web.qingqiu import qingqiu


if __name__=='__main__':
    #登录流程
    url = 'http://172.29.19.92:8989/siteapi/oneid/ucenter/login/'
    logintoken=qingqiu().postlogin(url)
    print(logintoken)

    #获取arkid所有用户流程
    url="http://172.29.19.92:8989/siteapi/oneid/user/?page=1&page_size=100&keyword="
    user_info=qingqiu().search_user(url,logintoken)
    print(user_info)

    ''' 
    #新增arkid用户流程
    url="http://172.29.19.92:8989/siteapi/oneid/user/"
    name="sectest"
    password="mima0203"
    add_info=qingqiu().add_user(url,logintoken,name,password)
    print(add_info)
    '''

    # 删除arkid用户流程
    url="http://172.29.19.92:8989/siteapi/oneid/user/"
    user="zhou11"
    del_user_info = qingqiu().del_user(url,logintoken,user)
    print(del_user_info)







