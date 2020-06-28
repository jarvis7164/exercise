#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 14:40
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : C-FIND_W.py
# @Software: PyCharm

from pydicom.dataset import Dataset
from pydicom.uid import (
    ImplicitVRLittleEndian,
    ExplicitVRLittleEndian,
    ExplicitVRBigEndian)
from pynetdicom import AE
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind
from pynetdicom.sop_class import BasicWorklistManagementServiceClass
from pynetdicom import AE, BasicWorklistManagementPresentationContexts

# Initialise the Application Entity
ae = AE(ae_title=b'PYNETDICOM')
# VerificationSOPClas'1.2.840.10008.3.1.1.1'#
ae.add_requested_context('1.2.840.10008.5.1.4.31',
[ImplicitVRLittleEndian,
ExplicitVRLittleEndian,
  ExplicitVRBigEndian])

# Create our Identifier (query) dataset
ds = Dataset()
ds.PatientName = ''
# ds.PatientID ='2019052700000014'
ds.ScheduledProcedureStepStartDate = "20190526"

print(ds)
# Associate with peer AE at IP 127.0.0.1 and port 11112
assoc = ae.associate('192.168.1.18', 1006, ae_title=b'eWordWL')

if assoc.is_established:
    # Use the C-FIND service to send the identifier
    responses = assoc.send_c_find(ds, msg_id=1, priority=2, query_model='W')
    for (status, identifier) in responses:
        if status:
            print('C-FIND query status: 0x{0:04x}'.format(status.Status))

                # If the status is 'Pending' then identifier is the C-FIND response
        if status.Status in (0xFF00, 0xFF01):
            print(identifier)
        else:
            print('Connection timed out, was aborted or received invalid response')

        # Release the association
    assoc.release()
else:
    print('Association rejected, aborted or never connected')
