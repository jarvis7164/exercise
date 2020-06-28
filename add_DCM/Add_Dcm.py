#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 14:07
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : Add_Dcm.py
# @Software: PyCharm

import os

def replace_suffix(filedir, suffix):
    files = os.listdir(filedir)
    num = 0
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] != suffix:
            newname = portion[0] + suffix
            filename = filedir + '\\' +filename
            newname = filedir + '\\' +newname
            os.rename(filename, newname)
            print("替换文件后缀", filename)
            num = num + 1
            print(num)
if __name__ == '__main__':
        replace_suffix('//192.168.1.55/testdemo/image/imcis_image/1006940574', '.dcm')