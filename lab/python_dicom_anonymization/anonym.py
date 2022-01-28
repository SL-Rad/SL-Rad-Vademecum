import tempfile
import numpy
import pydicom

import numpy as np
from pydicom import dcmread

DICOM_file_path = 'lab\python_dicom_anonymization\dicom\DICOM_sample.DCM'

DICOM_file = dcmread(DICOM_file_path)
print(DICOM_file)
