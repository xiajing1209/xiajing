# -*- coding: UTF-8 -*-
import requests,json


# session管理
session=requests.session()
#auth发包
res=session.post('http://112.74.191.10/inter/HTTP/auth')
print(res.text)
jsonres=json.loads(res.text)
# jsonres=eval(res.text)
print(jsonres['token'])

# 添加头
session.headers['token']=jsonres['token']

#构造参数
params={
    'username':'xia1',
    'pwd':'123456',
    'nickname':'测试账号',
    'describe':'描述'
}
# 注册发包
res=session.post('http://testingedu.com.cn/inter/HTTP/register',data=params)
print(res.text)

#构造参数
params={
    'username':'xia1',
    'password':'123456'
}
0#login发包
res=session.post('http://112.74.191.10/inter/HTTP/login',data=params)
print(res.text)


jsonres=json.loads(res.text)

#构造参数
params={
    'id':jsonres['userid']
}
#查看个人信息发包
res=session.post('http://testingedu.com.cn/inter/HTTP/getUserInfo',data=params)
print(res.text)
#退出发包
res=session.post('http://testingedu.com.cn/inter/HTTP/logout')
print(res.text)