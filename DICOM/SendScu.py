#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 14:00
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : SendScu.py
# @Software: PyCharm

#发送C-ECHO校验
from pynetdicom import AE
from pynetdicom.sop_class import VerificationSOPClass

# Initialise the Application Entity
ae = AE("JM_SCU")

# Add a requested presentation context
ae.add_requested_context(VerificationSOPClass)

# Associate with peer AE at IP 127.0.0.1 and port 11112
assoc = ae.associate('127.0.0.1', 318,ae_title='HYSERVICE')

if assoc.is_established:
    # Use the C-ECHO service to send the request
    # returns the response status a pydicom Dataset
    status = assoc.send_c_echo()

    # Check the status of the verification request
    if status:
        # If the verification request succeeded this will be 0x0000
        print('C-ECHO request status: 0x{0:04x}'.format(status.Status))
    else:
        print('Connection timed out, was aborted or received invalid response')

    # Release the association
    assoc.release()
else:
    print('Association rejected, aborted or never connected')