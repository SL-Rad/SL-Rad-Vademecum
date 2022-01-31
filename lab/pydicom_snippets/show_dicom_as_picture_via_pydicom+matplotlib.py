# Tutorial:
# https://pastebin.com/MXkpnAmq
# https://www.youtube.com/watch?v=hWwAFNmPZFQ

# Importa le library
import matplotlib.pyplot as plt
import numpy as np
from pydicom import dcmread

# Definisci dove si trova il file
DICOM_file_path = 'lab\python_dicom_anonymization\dicom\ddd.DCM'

# Definisci il file
DICOM_file = dcmread(DICOM_file_path)

# Mostra il file dicom come immagine
plt.imshow(DICOM_file.pixel_array, cmap=plt.cm.gray)
plt.show()
