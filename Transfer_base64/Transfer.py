#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 16:55
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : Transfer.py
# @Software: PyCharm
import json

import requests
import os, base64
#获取token
def get_token():
	header = {'Content-Type': 'application/json'}
	url = "http://192.168.1.18:8703/Token/Retrive"  # token服务器地址
	payload = {
		"requestIP": "192.168.1.58",  # 请求客户端
		"audience": "eWordRIS",
		"customData": {},
		"expire": 240}
	res = requests.post(url, headers=header, json=payload)
	return res.json()['token']

#调用RIS接口获取图文报告的BASE64数据
headers = {'Content-Type':'application/json',
			'Authorization': get_token()}
body ={
	"FillerOrderID":"AA7D3156-77DA-47CB-9B7D-ABE300C16391",
	"OrganizationCode":"dysrmyy"
}
url = "http://192.168.1.18:8141/api/ReportFile/Get"

r = requests.post(url,headers=headers,json=body)
# print(r.content,type(r.content))
r_dict = json.loads(r.content)
# print(r_dict["data"],type(r_dict["data"]))
list = []
for i in r_dict["data"]:
	data = i["reportFile"]
	list.append(data)

#将获取的BASE64编码转成JPG图片并保存到指定路径
for i in range(0,len(list)):
	img_data = base64.b64decode(list[i])
	with open("{0}.jpg".format(i),"wb") as f:
		f.write(img_data)
	print("successful")

