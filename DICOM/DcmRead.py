#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 10:36
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : DcmRead.py
# @Software: PyCharm

import pydicom
from pydicom import dcmread
filename = r"D:\Python\exercise\DICOM\1.76.380.18.14.1170612122453859.13849.92.524.dcm"
dataset = dcmread(filename)
print(dataset.pixel_array)