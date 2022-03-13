import os  # Importa la library os necessaria per interaggie con il sistema operativo
import re  # importa la library re necessaria per utilizzare regex

cerca_rx = 'RX'
cerca_rx_cranio = 'RX CRANIO'
cerca_rx_teleradiografia = 'RX TELERADIOGRAFIA'
cerca_rx_naso = 'RX OSSA NASALI'
cerca_rx_opt = 'OPT ARCATE DENTARIE'
cerca_rx_teleradiografia_cranio = 'RX TELERADIOGRAFIA LAT. DEL CRANIO'
cerca_rx_trachea = 'RX TRACHEA'
cerca_rx_torace = 'RX TORACE'
cerca_rx_torace_laterale = 'RX TORACE + LATERALE'
cerca_rx_torace_letto = 'RX TORACE AL LETTO'
cerca_rx_sterno = 'RX STERNO'
cerca_rx_costato = 'RX EMICOSTATO'
cerca_rx_clavicola = 'RX CLAVICOLA'
cerca_rx_spalla = 'RX SPALLA'
cerca_rx_omero = 'RX OMERO'
cerca_rx_gomito = 'RX GOMITO'
cerca_rx_avambraccio = 'RX AVAMBRACCIO'
cerca_rx_polso = 'RX POLSO'
cerca_rx_mano = 'RX MANO'
cerca_rx_colonna_c = 'RX COLONNA CERVICALE'
cerca_rx_colonna_d = 'RX COLONNA DORSALE'
cerca_rx_colonna_l = 'RX COLONNA LOMBOSACRALE'
cerca_rx_colonna_s = 'RX COLONNA SACRO'
cerca_rx_colonna_in_toto = 'RX COLONNA IN TOTO'
cerca_rx_colonna_oblique = '+OBLIQUE'
cerca_rx_colonna_funzionali = '+FUNZIONALI'
cerca_rx_colonna_s_dinamiche = 'RADIOGRAFIA DEL RACHIDE LOMBO SACRALE DINAMICA'
cerca_rx_colonna_morfometria = 'X MORFOMETRIA'
cerca_rx_telecolonna_ortostatismo = 'RX TELECOLONNA IN ORTOSTATISMO'
cerca_rx_addome = 'RX ADDOME'
cerca_rx_bacino = 'RX BACINO'
cerca_rx_anca = 'RX ANCA'
cerca_rx_arti_inf = 'RX ARTI INF. E BACINO SOTTO CARICO'
cerca_rx_rotula = 'RX ASSIALE DI ROTULE (1 PROIEZ.)'
cerca_rx_rotule_30_60_90 = 'RX ASSIALI DI ROTULA 30 60 90'
cerca_rx_femore = 'RX FEMORE'
cerca_rx_gamba = 'RX GAMBA'
cerca_rx_ginocchio = 'RX GINOCCHIO'
cerca_rx_caviglia = 'RX CAVIGLIA'
cerca_rx_piede = 'RX PIEDE'
cerca_rx_piede_carico = 'SOTTO CARICO'
cerca_rx_altro = 'ALTRA RADIOGRAFIA (RX) DELLO SCHELETRO TORACICO COSTALE MONOLATERALE'
cerca_rx_toto = 'RX RADIOGRAFIA SCHELETRO IN TOTO'

cerca_transito_gastroesofageo = 'RX ESOFAGO STOMACO E DUODENO'
cerca_ileografia = 'TUBO DIGERENTE CON MDC IDROSOLUBILE'


cerca_ecografia = 'ECOGRAFIA'
cerca_ecografia_doppler = 'ECO-DOPPLER'
cerca_ecografia_salivari = 'ECOGRAFIA GHIANDOLE SALIVARI'
cerca_ecografia_sottomandibolare = 'ECOGRAFIA SOTTOMANDIBOLARE'
cerca_ecografia_doppler_tsa_1 = 'ECO-COLOR DOPPLER TSA'
cerca_ecografia_doppler_tsa_2 = 'ECO-DOPPLER TRONCHI SOVRAORTICI'
cerca_ecografia_tiroide = 'ECOGRAFIA TIROIDE'
cerca_ecografia_doppler_tiroide = 'ECOGRAFIA/DOPPLER TIROIDE-PARATIROIDI'
cerca_ecografia_collo = 'ECOGRAFIA DEL COLLO'
cerca_ecografia_mammaria = 'ECOGRAFIA MAMMARIA'
cerca_ecografia_torace = 'ECOGRAFIA TORACICA'
cerca_ecografia_spalla = 'ECOGRAFIA SPALL'
cerca_ecografia_ascellare = 'ECOGRAFIA ASCELLARE'
cerca_ecografia_polso = 'ECOGRAFIA POLSO'
cerca_ecografia_addome = 'ECOGRAFIA ADDOME'
cerca_ecografia_addome_completo = 'ECOGRAFIA ADDOME COMPLETO'
cerca_ecografia_addome_completo_rpm = 'ECOGRAFIA ADDOME COMPLETO CON R.P.M.'
cerca_ecografia_addome_superiore = 'ECOGRAFIA ADDOME SUPERIORE'
cerca_ecografia_addome_inferiore = 'ECOGRAFIA ADDOME INFERIORE'
cerca_ecografia_anca = 'ECOGRAFIA ANCA'
cerca_ecografia_epatica = 'ECOGRAFIA EPATICA'
cerca_ecografia_epatopancreatica = 'ECOGRAFIA EPATOPANCREATICA'
cerca_ecografia_intestinale = 'ECOGRAFIA INTESTINALE'
cerca_ecografia_renovescicale_1 = 'ECOGRAFIA RENO-VESCICALE'
cerca_ecografia_renovescicale_2 = 'ECOGRAFIA RENO VESCICALE'
cerca_ecografia_renovescicale_3 = 'ECOGRAFIA RENOVESCICALE'
cerca_ecografia_renale = 'ECOGRAFIA RENALE'
cerca_ecografia_doppler_renale = 'ECO-DOPPLER RENALE'
cerca_ecografia_mdc_1 = 'ECOGRAFIA CON M.D.C.'
cerca_ecografia_mdc_2 = 'ECO ADD.COMPL. CON CONTRASTO'
cerca_ecografia_muscolotendinea = 'ECOGRAFIA MUSCOLO-TENDINEA'
cerca_ecografia_osteoarticolare = 'ECOGRAFIA OSTEOARTICOLARE'
cerca_ecografia_tessuti_superficiali = 'ECOGRAFIA TESSUTI SUPERFICIALI'
cerca_ecografia_tessuti_molli = 'ECOGRAFIA TESSUTI MOLLI'
cerca_ecografia_inguinale = 'ECOGRAFIA REGIONI INGUINALI'
cerca_ecografia_testicolare = 'ECOGRAFIA TESTICOLARE'
cerca_ecografia_scrotale = 'ECOGRAFIA SCROTALE'
cerca_ecografia_pene = 'ECOGRAFIA PENIENA'
cerca_ecografia_aaii_1 = 'ECOGRAFIA ARTI INFERIORI'
cerca_ecografia_aaii_2 = 'ECOGRAFIA ARTO INFERIORE'
cerca_ecografia_doppler_venosa = 'ECO-DOPPLER VENOSO'
cerca_ecografia_tendine_achille = 'ECOGRAFIA TENDINE ACHILLE'
cerca_ecografia_transrettale = 'ECOGRAFIA TRANSRETTALE'

cerca_consulenza = 'CONSULENZA RADIOLOGICA'
cerca_controllo_radiologico = 'VISITA RADIOLOGICA DI CONTROLLO'
cerca_agobiopsia = 'AGOBIOPSIA'
cerca_agobiopsia_tc = 'AGOBIOPSIA TC'
cerca_agobiopsia_tc_sedi_profonde = 'AGOBIOPSIA TC GUIDATA SEDI PROF'
cerca_agobiopsia_eco_sedi_profonde = 'AGOBIOPSIA ECOGUID. SEDI PROF'
cerca_agobiopsia_mammaria = 'AGOBIOPSIA MAMMARIA'
cerca_agobiopsia_toracica = 'AGOBIOPSIA TORACICA'
cerca_agobiopsia_epatica = 'AGOBIOPSIA EPATICA'
cerca_agobiopsia_eco_rene = 'AGOBIOPSIA ECOGUID. RENE'
cerca_radiofrequenze = 'RADIOFREQUENZ'
cerca_drenaggio = 'DRENAGGIO'

cerca_tomografia = 'TC'
cerca_tc_cranio = 'TC CRANIO'
cerca_tc_cranio_con_mdc = 'TC CRANIO CON MDC'
cerca_tc_orbite = 'TC ORBITE'
cerca_tc_rocche_mastoidi = 'TC ROCCHE MASTOIDI'
cerca_tc_rocche_mastoidi_con_mdc = 'TC ROCCHE MASTOIDI CON MDC'
cerca_tc_massiccio_facciale = 'TC MASSICCIO FACCIALE'
cerca_tc_massiccio_facciale_con_mdc = 'TC MASSICCIO FACCIALE CON MDC'
cerca_tc_collo = 'TC COLLO'
cerca_tc_collo_con_mdc = 'TC COLLO CON MDC'
cerca_tc_torace = 'TC TORACE'
cerca_tc_torace_con_mdc = 'TC TORACE CON MDC'
cerca_tc_torace_ad_alta_risoluzione = 'TC TORACE AD ALTA RISOLUZIONE'
cerca_tc_spalla = 'TC SPALLA'
cerca_tc_spalla_e_braccio = 'TC SPALLA E BRACCIO'
cerca_tc_gomito_e_avambraccio = 'TC GOMITO E AVAMBRACCIO'
cerca_tc_polso_e_mano = 'TC POLSO E MANO'
cerca_angio_tc = 'ANGIO TC'
cerca_angio_tc_addome = 'ANGIO TC ADDOME'
cerca_angio_tc_altro_distretto = 'ANGIO TC ALTRO DISTRETTO'
cerca_angio_tc_torace = 'ANGIO TC TORACE'
cerca_angio_tc_aorta = 'ANGIO TC AORTA'
cerca_angio_tc_encefalo = 'ANGIO TC ENCEFALO'
cerca_tac_coronarica = 'TAC CORONARICA'
cerca_cardio_tc = 'CARDIO-TC'
cerca_tc_colonna_cervicale = 'TC COLONNA CERVICALE'
cerca_tc_colonna_cervicale_con_mdc = 'TC COLONNA CERVICALE CON MDC'
cerca_tc_colonna_dorsale = 'TC COLONNA DORSALE'
cerca_tc_colonna_dorsale_con_mdc = 'TC COLONNA DORSALE CON MDC'
cerca_tc_colonna_dorsale_e_lombare = 'TC COLONNA DORSALE E LOMBARE'
cerca_tc_colonna_lombare = 'TC COLONNA LOMBARE'
cerca_tc_addome = 'TC ADDOME'
cerca_tc_addome_completo = 'TC ADDOME COMPLETO'
cerca_tc_addome_sup = 'TC ADDOME SUP'
cerca_tc_addome_sup_con_mdc = 'TC ADDOME SUP. CON MDC'
cerca_tc_addome_inf = 'TC ADDOME INF'
cerca_tc_addome_inf_con_mdc = 'TC ADDOME INF. CON MDC'
cerca_tc_addome_completo_con_mdc = 'TC ADDOME COMPLETO CON MDC'
cerca_colonscopia_virtuale = 'COLONSCOPIA VIRTUALE'
cerca_tc_surreni = 'TC SURRENI'
cerca_tc_surrene_ad_alta_risoluzione = 'TC SURRENE AD ALTA RISOLUZIONE'
cerca_tc_reni_surreni = 'TC RENI-SURRENI'
cerca_tc_apparato_urinario = 'TC APPARATO URINARIO'
cerca_cistotc = 'CISTOTC'
cerca_tc_bacino = 'TC BACINO'
cerca_tc_coxo_femorale = 'TC COXO-FEMORALE'
cerca_tc_ginocchio_e_gamba = 'TC GINOCCHIO E GAMBA'
cerca_tc_caviglia_e_piede = 'TC CAVIGLIA E PIEDE'


cerca_ = cerca_rm = 'RM'
cerca_rm_encefalo = 'RM ENCEFALO'
cerca_rm_encefalo_con_mdc = 'RM ENCEFALO CON MDC'
cerca_rm_ipofisi = 'RM IPOFISI'
cerca_rm_massiccio_facciale = 'RM MASSICCIO FACCIALE'
cerca_rm_sclerosi_multipla = 'RM SCLEROSI MULTIPLA'
cerca_rm_collo = 'RM COLLO'
cerca_rm_del_collo = 'RM DEL COLLO'
cerca_rm_muscoli_cervicali = 'RM MUSCOLI CERVICALI'
cerca_rm_colonna_cervicale = 'RM COLONNA CERVICALE'
cerca_rm_colonna_toracica = 'RM COLONNA TORACICA'
cerca_rm_colonna_dorsale = 'RM COLONNA DORSALE'
cerca_rm_colonna_lombosacrale = 'RM COLONNA LOMBOSACRALE'
cerca_rm_colonna_in_toto = 'RM COLONNA IN TOTO'
cerca_rm_colonna_per_midollo_spinale = 'RM COLONNA PER MIDOLLO SPINALE'
cerca_rm_midollo_spinale = 'RM MIDOLLO SPINALE'
cerca_angio_rm = 'ANGIO RM'
cerca_angio_rm_del_distr_vasc_intracr = 'ANGIO RM DEL DISTR. VASC.INTRACR'
cerca_angio_rm_intracranica = 'ANGIO RM INTRACRANICA'
cerca_angio_rm_vasi_del_collo = 'ANGIO RM VASI DEL COLLO'
cerca_angio_rm_addome = 'ANGIO RM ADDOME'
cerca_rm_torace = 'RM TORACE'
cerca_rm_mediastino = 'RM MEDIASTINO'
cerca_rm_cuore = 'RM CUORE'
cerca_rm_parete_toracica = 'RM PARETE TORACICA'
cerca_rm_spalla = 'RM SPALLA'
cerca_rm_braccio = 'RM BRACCIO'
cerca_rm_gomito = 'RM GOMITO'
cerca_rm_avambraccio = 'RM AVAMBRACCIO'
cerca_rm_diaframma = 'RM DIAFRAMMA'
cerca_rm_epatica = 'RM EPATICA'
cerca_colangio_rm = 'COLANGIO RM'
cerca_rm_delladdome = 'RM DELL\'ADDOME'
cerca_rm_delladdome_sup_inf = 'RM DELL\'ADDOME SUP.+INF'
cerca_rm_addome_superiore = 'RM ADDOME SUPERIORE'
cerca_rm_addome_sup = 'RM ADDOME SUP'
cerca_rm_delladdome_sup = 'RM DELL\'ADDOME SUP'
cerca_rm_addome_inferiore = 'RM ADDOME INFERIORE'
cerca_rm_add_inf = 'RM ADD.INF'
cerca_rm_delladdome_inf = 'RM DELL\'ADDOME INF.'
cerca_rm_surreni = 'RM SURRENI'
cerca_enterorm = 'ENTERORM'
cerca_entero_rm1 = 'ENTERO RM'
cerca_entero_rm2 = 'ENTERO-RM'
cerca_defecografia_rm = 'DEFECOGRAFIA RM'
cerca_rm_defecografica = 'RM DEFECOGRAFICA'
cerca_rm_del_pene = 'RM DEL PENE'
cerca_rm_loggia_prostatica_con_mdc = 'RM LOGGIA PROSTATICA CON MDC'
cerca_rm_multiparametrica_della_loggia_prostatica = 'RM MULTIPARAMETRICA DELLA LOGGIA PROSTATICA'
cerca_rm_multiparametrica_della_prostata = 'RM MULTIPARAMETRICA DELLA PROSTATA'
cerca_rm_multiparametrica_prostatica = 'RM MULTIPARAMETRICA PROSTATICA'
cerca_rm_pelvi = 'RM PELVI'
cerca_rm_parete_addominale = 'RM PARETE ADDOMINALE'
cerca_rm_bacino = 'RM BACINO'
cerca_rm_femore = 'RM FEMORE'
cerca_rm_gamba = 'RM GAMBA'
cerca_rm_coscia = 'RM COSCIA'
cerca_rm_ginocchio = 'RM GINOCCHIO'
cerca_rm_caviglia = 'RM CAVIGLIA'
cerca_rm_piede = 'RM PIEDE'
cerca_rm_ren = 'RM REN'

cerca_scintigrafia = 'SCINTIGRAFIA'


# prendi tutti i file(filename) conxtenuti nella directory(os.listdir)
for filename in os.listdir('4_dir_referti_txt_anonimizzati_senza_TSRM'):
    if filename.endswith('.txt'):  # che terminano con .txt (filename.endswith)
        with open(os.path.join('4_dir_referti_txt_anonimizzati_senza_TSRM', filename), encoding="Latin-1") as f:
            testo_del_referto = f.read()
                  
            if re.search(cerca_rx, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_cranio, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_cranio + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_teleradiografia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_teleradiografia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_naso, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_naso + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_opt, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_opt + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_teleradiografia_cranio, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_teleradiografia_cranio + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_trachea, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_trachea + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_torace, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_torace + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_torace_laterale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_torace_laterale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_torace_letto, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_torace_letto + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_sterno, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_sterno + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_costato, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_costato + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_clavicola, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_clavicola + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_spalla, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_spalla + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_omero, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_omero + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_gomito, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_gomito + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_avambraccio, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_avambraccio + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_polso, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_polso + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_mano, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_mano + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_colonna_c, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_colonna_c + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_colonna_d, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_colonna_d + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_colonna_l, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_colonna_l + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_colonna_s, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_colonna_s + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_colonna_in_toto, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_colonna_in_toto + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_colonna_oblique, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_colonna_oblique + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_colonna_funzionali, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_colonna_funzionali + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_colonna_s_dinamiche, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_colonna_s_dinamiche + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_colonna_morfometria, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_colonna_morfometria + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_telecolonna_ortostatismo, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_telecolonna_ortostatismo + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_addome, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_addome + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_bacino, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_bacino + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_anca, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_anca + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_arti_inf, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_arti_inf + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_rotula, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_rotula + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_rotule_30_60_90, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_rotule_30_60_90 + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_femore, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_femore + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_gamba, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_gamba + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_ginocchio, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_ginocchio + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_caviglia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_caviglia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_piede, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_piede + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_piede_carico, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_piede_carico + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_altro, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_altro + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rx_toto, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rx_toto + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_transito_gastroesofageo, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_transito_gastroesofageo + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ileografia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ileografia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_doppler, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_doppler + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_salivari, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_salivari + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_sottomandibolare, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_sottomandibolare + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_doppler_tsa_1, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_doppler_tsa_1 + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_doppler_tsa_2, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_doppler_tsa_2 + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_tiroide, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_tiroide + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_doppler_tiroide, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_doppler_tiroide + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_collo, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_collo + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_mammaria, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_mammaria + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_torace, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_torace + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_spalla, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_spalla + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_ascellare, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_ascellare + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_polso, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_polso + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_addome, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_addome + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_addome_completo, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_addome_completo + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_addome_completo_rpm, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_addome_completo_rpm + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_addome_superiore, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_addome_superiore + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_addome_inferiore, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_addome_inferiore + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_anca, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_anca + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_epatica, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_epatica + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_epatopancreatica, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_epatopancreatica + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_intestinale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_intestinale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_renovescicale_1, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_renovescicale_1 + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_renovescicale_2, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_renovescicale_2 + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_renovescicale_3, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_renovescicale_3 + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_renale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_renale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_doppler_renale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_doppler_renale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_mdc_1, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_mdc_1 + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_mdc_2, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_mdc_2 + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_muscolotendinea, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_muscolotendinea + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_osteoarticolare, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_osteoarticolare + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_tessuti_superficiali, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_tessuti_superficiali + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_tessuti_molli, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_tessuti_molli + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_inguinale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_inguinale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_testicolare, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_testicolare + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_scrotale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_scrotale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_pene, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_pene + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_aaii_1, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_aaii_1 + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_aaii_2, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_aaii_2 + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_doppler_venosa, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_doppler_venosa + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_tendine_achille, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_tendine_achille + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_ecografia_transrettale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ecografia_transrettale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_consulenza, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_consulenza + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_controllo_radiologico, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_controllo_radiologico + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_agobiopsia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_agobiopsia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_agobiopsia_tc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_agobiopsia_tc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_agobiopsia_tc_sedi_profonde, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_agobiopsia_tc_sedi_profonde + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_agobiopsia_eco_sedi_profonde, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_agobiopsia_eco_sedi_profonde + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_agobiopsia_mammaria, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_agobiopsia_mammaria + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_agobiopsia_toracica, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_agobiopsia_toracica + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_agobiopsia_epatica, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_agobiopsia_epatica + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_agobiopsia_eco_rene, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_agobiopsia_eco_rene + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_radiofrequenze, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_radiofrequenze + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_drenaggio, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_drenaggio + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tomografia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tomografia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_cranio, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_cranio + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_cranio_con_mdc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_cranio_con_mdc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_orbite, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_orbite + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_rocche_mastoidi, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_rocche_mastoidi + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_rocche_mastoidi_con_mdc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_rocche_mastoidi_con_mdc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_massiccio_facciale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_massiccio_facciale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_massiccio_facciale_con_mdc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_massiccio_facciale_con_mdc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_collo, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_collo + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_collo_con_mdc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_collo_con_mdc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_torace, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_torace + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_torace_con_mdc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_torace_con_mdc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_torace_ad_alta_risoluzione, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_torace_ad_alta_risoluzione + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_spalla, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_spalla + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_spalla_e_braccio, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_spalla_e_braccio + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_gomito_e_avambraccio, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_gomito_e_avambraccio + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_polso_e_mano, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_polso_e_mano + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_angio_tc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_angio_tc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_angio_tc_addome, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_angio_tc_addome + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_angio_tc_altro_distretto, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_angio_tc_altro_distretto + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_angio_tc_torace, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_angio_tc_torace + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_angio_tc_aorta, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_angio_tc_aorta + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_angio_tc_encefalo, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_angio_tc_encefalo + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tac_coronarica, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tac_coronarica + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_cardio_tc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_cardio_tc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_colonna_cervicale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_colonna_cervicale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_colonna_cervicale_con_mdc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_colonna_cervicale_con_mdc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_colonna_dorsale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_colonna_dorsale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_colonna_dorsale_con_mdc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_colonna_dorsale_con_mdc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_colonna_dorsale_e_lombare, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_colonna_dorsale_e_lombare + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_colonna_lombare, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_colonna_lombare + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_addome, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_addome + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_addome_completo, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_addome_completo + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_addome_sup, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_addome_sup + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_addome_sup_con_mdc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_addome_sup_con_mdc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_addome_inf, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_addome_inf + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_addome_inf_con_mdc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_addome_inf_con_mdc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_addome_completo_con_mdc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_addome_completo_con_mdc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_colonscopia_virtuale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_colonscopia_virtuale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_surreni, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_surreni + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_surrene_ad_alta_risoluzione, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_surrene_ad_alta_risoluzione + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_reni_surreni, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_reni_surreni + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_apparato_urinario, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_apparato_urinario + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_cistotc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_cistotc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_bacino, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_bacino + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_coxo_femorale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_coxo_femorale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_ginocchio_e_gamba, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_ginocchio_e_gamba + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_tc_caviglia_e_piede, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_tc_caviglia_e_piede + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_ + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_encefalo, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_encefalo + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_encefalo_con_mdc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_encefalo_con_mdc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_ipofisi, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_ipofisi + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_massiccio_facciale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_massiccio_facciale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_sclerosi_multipla, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_sclerosi_multipla + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_collo, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_collo + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_del_collo, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_del_collo + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_muscoli_cervicali, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_muscoli_cervicali + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_colonna_cervicale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_colonna_cervicale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_colonna_toracica, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_colonna_toracica + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_colonna_dorsale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_colonna_dorsale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_colonna_lombosacrale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_colonna_lombosacrale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_colonna_in_toto, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_colonna_in_toto + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_colonna_per_midollo_spinale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_colonna_per_midollo_spinale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_midollo_spinale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_midollo_spinale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_angio_rm, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_angio_rm + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_angio_rm_del_distr_vasc_intracr, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_angio_rm_del_distr_vasc_intracr + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_angio_rm_intracranica, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_angio_rm_intracranica + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_angio_rm_vasi_del_collo, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_angio_rm_vasi_del_collo + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_angio_rm_addome, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_angio_rm_addome + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_torace, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_torace + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_mediastino, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_mediastino + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_cuore, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_cuore + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_parete_toracica, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_parete_toracica + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_spalla, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_spalla + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_braccio, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_braccio + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_gomito, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_gomito + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_avambraccio, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_avambraccio + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_diaframma, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_diaframma + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_epatica, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_epatica + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_colangio_rm, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_colangio_rm + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_delladdome, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_delladdome + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_delladdome_sup_inf, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_delladdome_sup_inf + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_addome_superiore, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_addome_superiore + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_addome_sup, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_addome_sup + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_delladdome_sup, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_delladdome_sup + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_addome_inferiore, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_addome_inferiore + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_add_inf, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_add_inf + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_delladdome_inf, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_delladdome_inf + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_surreni, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_surreni + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_enterorm, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_enterorm + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_entero_rm1, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_entero_rm1 + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_entero_rm2, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_entero_rm2 + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_defecografia_rm, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_defecografia_rm + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_defecografica, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_defecografica + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_del_pene, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_del_pene + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_loggia_prostatica_con_mdc, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_loggia_prostatica_con_mdc + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_multiparametrica_della_loggia_prostatica, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_multiparametrica_della_loggia_prostatica + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_multiparametrica_della_prostata, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_multiparametrica_della_prostata + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_multiparametrica_prostatica, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_multiparametrica_prostatica + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_pelvi, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_pelvi + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_parete_addominale, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_parete_addominale + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_bacino, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_bacino + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_femore, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_femore + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_gamba, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_gamba + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_coscia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_coscia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_ginocchio, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_ginocchio + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_caviglia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_caviglia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_piede, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_piede + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_ren, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_ren + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_scintigrafia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_scintigrafia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_gamba, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_gamba + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_coscia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_coscia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_ginocchio, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_ginocchio + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_caviglia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_caviglia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_piede, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_piede + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_rm_ren, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_rm_ren + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

            if re.search(cerca_scintigrafia, testo_del_referto):
                newfilename_post_edit = filename[:-4] + "_" + cerca_scintigrafia + ".txt"
                with open('5_dir_referti_txt_anonimizzati_senza_TSRM_filtrati/' + newfilename_post_edit, 'w') as i:
                    i.write(testo_del_referto)

