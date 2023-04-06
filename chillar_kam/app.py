from img2table.document import PDF, Image
from img2table.ocr import TesseractOCR

# Instantiation of the pdf
img = Image(src="cropped/202_cropped_out.png")

# Instantiation of the OCR, Tesseract, which requires prior installation
ocr = TesseractOCR(lang="eng")

# Table identification and extraction
pdf_tables = img.extract_tables(ocr=ocr)

# We can also create an excel file with the tables
img.to_xlsx('tables.xlsx', ocr=ocr)