# Tutorial:
# https://pastebin.com/MXkpnAmq
# https://www.youtube.com/watch?v=hWwAFNmPZFQ

# Importa le library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pydicom import dcmread
import datetime
import os

# Definisci dove si trova il file
DICOM_file_path = 'lab\python_dicom_anonymization\dicom\DICOM_sample.DCM'

# Definisci il file
DICOM_file = dcmread(DICOM_file_path)

# Mostra il file dicom come immagine
plt.imshow(DICOM_file.pixel_array, cmap=plt.cm.gray)

your_data = DICOM_file.pixel_array
# can pass your own column names if needed
your_df = pd.DataFrame(your_data)
your_df.to_csv('lab/pydicom_snippets/output.csv')

# Stampa a schermo
print(DICOM_file.pixel_array)

# Esporta il data array in csv
now = datetime.datetime.now().strftime("%H.%M.%S_%m-%d-%Y")
os.rename('lab/pydicom_snippets/output.csv',
          'lab/pydicom_snippets/' + now + 'output.csv')
