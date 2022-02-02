# Importa le library
import numpy as np
from pydicom import dcmread

# Definisci dove si trova il file da anonimizzare
DICOM_file_path = 'lab\python_dicom_anonymization\dicom\DICOM_sample2.DCM'

# Definisci il file da anonimizzare
DICOM_to_anonym_file = dcmread(DICOM_file_path)

# Stampa a schermo le informazioni del dicom prima di anonimizzare
# print(DICOM_to_anonym_file)

###########################################################


# Modifica (0010,0020) l'elemento 'Patient ID'
DICOM_to_anonym_file.PatientID = "Anonymous_ID"
DICOM_to_anonym_file.save_as(
    "lab\python_dicom_anonymization\dicom\DICOM_sample_anonym.DCM")

now = datetime.datetime.now().strftime("%H.%M.%S_%m-%d-%Y")
anonym_tag = "_anonymous_"
os.rename('lab/python_dicom_anonymization/dicom/output.csv',
          'lab/python_dicom_anonymization/dicom/' + now + anonym_tag + 'output.csv')


###########################################################

# Definisci dove si trova il file anonimo
DICOM_file_path = 'lab\python_dicom_anonymization\dicom\DICOM_sample2.DCM'

# Definisci il file
DICOM_file = dcmread(DICOM_file_path)

# Mostra il file anonimizzato per valutare se realmente anonimo
print(DICOM_file)
