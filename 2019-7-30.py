#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 18:43
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : 2019-7-30.py
# @Software: PyCharm

# import urllib.parse
# import urllib.request
# #打开指定需要爬取的网页
# response = urllib.request.urlopen("http://www.baidu.com")
# html = response.read()   #读取网页内容
# print(html)

import requests

response = requests.get("http://www.baidu.com")
response.encoding = 'uft-8'  #解决中文乱码的问题
print(response.status_code) #打印状态码
print(response.url) #打印请求url
print(response.headers)  #打印头部信息
print(response.cookies) #打印cookie信息
print(response.text)    #以文本形式打印网页源码
print(response.content) #以字节流的形式打印网页源码