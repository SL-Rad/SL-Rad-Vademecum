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

from DataScienceDeck.preprocessing.preprocessing import load_scan

pathway = 'lab\python_dicom_anonymization\dicom'

x = load_scan(pathway)
print(x)

# ????????????????????????????????????
