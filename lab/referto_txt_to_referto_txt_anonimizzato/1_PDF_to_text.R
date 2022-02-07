# Il programma definisce una cartella di lavoro, 
# successivamente definisce tutti i pdf presenti nell'elemento dest 
# successivamente ogni elemento presente in dest viene inserito all'internodella lista my files, 
# successivamente tutti gli elementi nella lista my files vengono trattati da parte del programma pdftotext.exe 
# che converte ogni pdf in un txt dallo stesso titolo nella stessa directory.

# Set work dir
#setwd("lab/referto_txt_to_referto_txt_anonimizzato/1_PDF_to_text.R")

# folder with 1000s of PDFs
dest <- "C:/Users/rusla/Desktop/referto_txt_to_referto_txt_anonimizzato/1_dir_referti_pdf_non_anonimi"

# make a vector of PDF file names
myfiles <- list.files(path = dest, pattern = "pdf",  full.names = TRUE)

# convert each PDF file that is named in the vector into a text file 
# text file is created in the same directory as the PDFs
# note that my pdftotext.exe is in a different location to yours
lapply(myfiles, function(i) system(paste('"C:/Program Files/XpdfReader/pdftotext.exe"', 
                                         paste0('"', i, '"')), wait = FALSE) )
    