# -*- coding: UTF-8 -*-
from inter.interkey import http

# 创建实例对象
tes=http()
# 设置基础地址
tes.seturl('http://112.74.191.10/inter/HTTP/')
# auth请求发包
tes.post('auth',None)
tes.savajson('token','token')
# 添加头token信息
tes.addhearder('token','{token}')
# 注册发包
tes.post('register','username=xia333&pwd=123456&nickname=测试账号&describe=描述')
# 登录发包
tes.post('login','username=xia333&password=123456')
tes.savajson('userid','userid')
# 查询个人信息发包
tes.post('getUserInfo','id={userid}')
# 退出
tes.post('logout',None)