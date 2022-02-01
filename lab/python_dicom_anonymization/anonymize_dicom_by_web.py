# Importa le library
import numpy as np
from pydicom import dcmread

# Definisci dove si trova il file
DICOM_file_path = 'lab\python_dicom_anonymization\dicom\DICOM_sample2.DCM'

# Definisci il file
DICOM_file = dcmread(DICOM_file_path)

# Apri il file Mostra le informazioni dentro il file dicom
print(DICOM_file)
