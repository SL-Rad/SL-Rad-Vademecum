# Tutorial:
# https://pastebin.com/MXkpnAmq
# https://www.youtube.com/watch?v=hWwAFNmPZFQ

# Importa le library
import numpy as np
from pydicom import dcmread

# Definisci dove si trova il file
DICOM_file_path = 'lab\python_dicom_anonymization\dicom\DICOM_sample2.DCM'

# Definisci il file
DICOM_file = dcmread(DICOM_file_path)

# Apri il file Mostra le informazioni dentro il file dicom
print(DICOM_file)

###########################################################


ds = dcmread("lab\python_dicom_anonymization\dicom\DICOM_sample.DCM")
# Edit the (0010,0020) 'Patient ID' element
ds.PatientID = "12345678"
ds.save_as("lab\python_dicom_anonymization\dicom\DICOM_sample2.DCM")

###########################################################

# Importa le library

# Definisci dove si trova il file
DICOM_file_path = 'lab\python_dicom_anonymization\dicom\DICOM_sample2.DCM'

# Definisci il file
DICOM_file = dcmread(DICOM_file_path)

# Apri il file Mostra le informazioni dentro il file dicom
print(DICOM_file)
