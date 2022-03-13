# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 09:58:05 2022

@author: R//S
"""

import os  # Importa la library os necessaria per interaggie con il sistema operativo
import re  # importa la library re necessaria per utilizzare regex

# definire la cartella da cui prendere i dati e quella in cui inserirli
# fare attenzione a inserire una / dopo il nome in modo che venga trattata come dir dal programma
origin_dir = '3_dir_referti_txt_anonimizzati/shutil/Referti_2020_txt_anonimizzati/'
destination_dir = '4_dir_referti_txt_anonimizzati_senza_TSRM/'

# prendi tutti i file(filename) contenuti nella directory(os.listdir)
for filename in os.listdir(origin_dir):
    if filename.endswith('.txt'):  # che terminano con .txt (filename.endswith)
        with open(os.path.join(origin_dir, filename)) as f:
            testo_del_referto_anonimizzato = f.read()

            # Trova il nome del tsrm e dei medici e rimuovili dal referto
            # Cancella tutto il testo compreso tra "Tecnico Sanitario di Radiologia Medica" e "Medico Chirurgo"
            testo_del_referto_anonimizzato_no_tsrm = re.sub("Tecnico Sanitario di Radiologia Medica[\s\S]*Medico Chirurgo",
                                                               "Medico Chirurgo", testo_del_referto_anonimizzato)

            # Cancella tutto il testo compreso tra "Medico Chirurgo" e "REFERTO FIRMATO DIGITALMENTE"
            # Se il comando precedente ha funzionato qusto sarà superfluo e non apporterà nessuma modicifica
            #referto_anonimizzato_completo = filename[:-4] + \
            #    "_anonimizzato_quasi_completo.txt"
            #testo_del_referto_no_name_no_med_end = re.sub("Medico Chirurgo[\s\S]*REFERTO FIRMATO DIGITALMENTE",
            #                                              "REFERTO FIRMATO DIGITALMENTE", testo_del_referto_no_name_no_tech_med_end)
            #referto_anonimizzato_completo = filename[:-4] + \
            #    "_anonimizzato_completo.txt"

            # Definisci il testo pre-edit
            #testo_pre_edit = testo_del_referto_no_name_no_med_end
            # testo_pre_edit = testo_del_referto_no_name

            # Rimuovi le righe di intestazione
            # testo_senza_intestazione = re.sub(
            #    "SERVIZIO SANITARIO REGIONE PIEMONTE[\s\S]*Data Nascita", "Data Nascita", testo_pre_edit)

            # Rimuovi le righe finali
            # testo_senza_pie_di_pagina = re.sub(
            #    "Sottoscritto digitalmente[\s\S]*documentazione radiologica precedente ad ogni nuovo esame", "", testo_senza_intestazione)

            # Definisci il testo da inviare in stampa nei file    
            Referto_anonimo_definitivo = testo_del_referto_anonimizzato_no_tsrm

            # A capo dopo il punto.
            # Refererto_post_edit_1 = re.sub(
            #    "\.", ".\n", Referto_anonimo_definitivo)

            # Rimuovi gli spazi bianchi dopo essere andati a capo
            # Refererto_post_edit_2 = re.sub(
            #    "\n ", "\n", Refererto_post_edit_1)

            # Definisci quale testo aggiungere in coda al nome del file
            newfilename_post_edit = filename[:-4] + "_anonimizzato_no_tsrm.txt"

            # Stampa i documenti modificati nella dir selezionata
            # Referto_definitivo_print = Refererto_post_edit_2
            Referto_definitivo_print = Referto_anonimo_definitivo
            # print(Referto_definitivo_print)
            with open(destination_dir + newfilename_post_edit, 'w') as i:
                i.write(Referto_definitivo_print)


