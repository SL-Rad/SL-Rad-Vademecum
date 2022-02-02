# SCRIPT FUNZIONANTE

# Importa le library
import numpy as np
from pydicom import dcmread

# Definisci dove si trova il file da anonimizzare
DICOM_file_path = 'lab\python_dicom_anonymization\\1_dicom_non_anonimizzati\DICOM_sample.DCM'

# Definisci il file da anonimizzare
DICOM_to_anonym_file = dcmread(DICOM_file_path)

# Stampa a schermo le informazioni del dicom prima di anonimizzare
print('non anonimizzato')
print(DICOM_to_anonym_file)

###########################################################


# Modifica (0010,0020) l'elemento 'Patient ID'
DICOM_to_anonym_file.PatientID = "Anonymous_ID"
DICOM_to_anonym_file.PatientName = "Anonymous"
DICOM_to_anonym_file.InstitutionName = "Anonymous"
DICOM_to_anonym_file.save_as(
    "lab\python_dicom_anonymization\\2_dicom_anonimizzati\DICOM_sample_anonymous.DCM")


###########################################################

# Definisci dove si trova il file anonimo
DICOM_anonymized_file_path = 'lab\python_dicom_anonymization\\2_dicom_anonimizzati\DICOM_sample_anonymous.DCM'

# Definisci il file
DICOM_anonymized_file = dcmread(DICOM_anonymized_file_path)

# Mostra il file anonimizzato per valutare se realmente anonimo
print('anonimizzato')
print(DICOM_anonymized_file)
