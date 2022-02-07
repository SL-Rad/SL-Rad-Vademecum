import pdftotext

# Load your PDF
with open("lab\referto_txt_to_referto_txt_anonimizzato\1_dir_referti_pdf_non_anonimi\Flat-panel_detector.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# If it's password-protected
# with open("secure.pdf", "rb") as f:
#    pdf = pdftotext.PDF(f, "secret")

# How many pages?
print(len(pdf))

# Iterate over all the pages
for page in pdf:
    print(page)

# Read some individual pages
print(pdf[0])
print(pdf[1])

# Read all the text into one string
print("\n\n".join(pdf))
