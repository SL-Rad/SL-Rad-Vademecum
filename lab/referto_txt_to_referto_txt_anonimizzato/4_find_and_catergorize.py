import os  # Importa la library os necessaria per interaggie con il sistema operativo
import re  # importa la library re necessaria per utilizzare regex

cerca_rx = 'RX'
cerca_ecografia = 'ECOGRAFIA'
cerca_tomografia = 'TC'
cerca_rm = 'RM'
cerca_scintigrafia = 'scintigrafia'

# prendi tutti i file(filename) conxtenuti nella directory(os.listdir)
for filename in os.listdir('4_dir_referti_txt_anonimizzati_senza_TSRM'):
    if filename.endswith('.txt'):  # che terminano con .txt (filename.endswith)
        with open(os.path.join('4_dir_referti_txt_anonimizzati_senza_TSRM', filename), encoding="Latin-1") as f:
            testo_del_referto = f.read()

            if re.search(cerca_rx, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)
                    
            if re.search(cerca_ecografia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)
                    
            if re.search(cerca_tomografia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tomografia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_scintigrafia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_scintigrafia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)