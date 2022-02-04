# PROGETTO SOSPESO - IN VALUTAZIONE

import os  # Importa la library os necessaria per interaggie con il sistema operativo
import numpy as np  # Importa la library numpy necessaria per _______
# Importa la funzione dcmread della library pydicom necessaria per leggere i file dicom
from pydicom import dcmread

# prendi tutti i file(filename) contenuti nella directory(os.listdir)
for filename in os.listdir('lab/python_dicom_anonymization/1_dicom_non_anonimizzati/sub/'):
    if filename.endswith('.DCM'):  # che terminano con .dcm (filename.endswith)
        with dcmread(filename) as f:
            f.PatientID = "Anonymous_ID_AAA"
            f.PatientName = "Anonymous_AAA"
            f.InstitutionName = "Anonymous_AAA"
            f.save_as(filename)
