import nibabel as nib
ct_img = nib.load("lab\dicom_sample\dicom1.DCM")
print(ct_img.header)
