# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 10:08:39 2022

@author: R//S
"""

import shutil # Libreria che permette di copiare i file
import os # Libreria di interazione tra python ed il sistema operativo

# Definisci la cartella da cui prendere i file
# NOTE:
# -nell'IDE spyder non importa usare le \\ } sarà l'ambiente da solo a provvedere
# -inserire la lettera r prima della stringa per fare si che questa venga letta come raw
src_dir = r'D:\#Medicina\#Radiodiagnostica\[#] Archivio Referti\#Referti 2020'

# Definisci la cartella da cui copiare i file; 
# la cartella non deve già esistere, sarà shutil a crearla
dest_dir = r'D:\#Medicina\#Radiodiagnostica\[#] Archivio Referti\#Anonimizzatore Referti (pdf-to-txt)\3_dir_referti_txt_anonimizzati\'

# getting all the files in the source directory
files = os.listdir(src_dir)

shutil.copytree(src_dir, dest_dir)
