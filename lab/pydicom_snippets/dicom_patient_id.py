from pydicom import dcmread

ds = dcmread("lab\python_dicom_anonymization\dicom\DICOM_sample.DCM")
# Edit the (0010,0020) 'Patient ID' element
ds.PatientID = "12345678"
ds.save_as("lab\python_dicom_anonymization\dicom\DICOM_sample.DCM")
