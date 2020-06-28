#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 14:46
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : C-Find.py
# @Software: PyCharm

from pydicom.dataset import Dataset

from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind

debug_logger()

ae = AE()
ae.add_requested_context(PatientRootQueryRetrieveInformationModelFind)

# Create our Identifier (query) dataset
ds = Dataset()
ds.PatientName = 'WangLiu'
ds.QueryRetrieveLevel = 'PATIENT'
# ds.SOPClassesInStudy = ''
# ds.PatientID = ''
# ds.StudyInstanceUID = ''
# ds.QueryRetrieveLevel = 'STUDY'

# Associate with the peer AE at IP 127.0.0.1 and port 11112
assoc = ae.associate('192.168.1.18', 1006,ae_title='eWordWL')
if assoc.is_established:
    # Send the C-FIND request
    responses = assoc.send_c_find(ds, PatientRootQueryRetrieveInformationModelFind)
    for (status, identifier) in responses:
        if status:
            print('C-FIND query status: 0x{0:04X}'.format(status.Status))
        else:
            print('Connection timed out, was aborted or received invalid response')

    # Release the association
    assoc.release()
else:
    print('Association rejected, aborted or never connected')