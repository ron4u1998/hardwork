import os


class AppConfig:
    UPLOAD_FOLDER     =   'documents'
    UPLOAD_EXTENSIONS =   [".pdf", ".PDF", ".jpeg", ".JPEG", ".jpg", ".JPG", ".PNG", ".png"]
    MODEL_PATH        =   'model/layoutlmv2_sam_ocr.pth'
    OUTPUT_PATH       =   'output'
    SECRET_KEY        =    os.urandom(24)
    DATA_DIR          =   'data'
    TESSERACT         =   'Tesseract/tesseract.exe'
    POPPLER           =   'poppler-0.68.0/bin'
    TEMP_DIR          =   'temporary'
    JSONFILEPATH      =   'info.json'
    FINAL_PATH        =   'final'
    EXCEL_FILES       =   'ExcelFolder'
    SAMPLE_IMAGE      =   'sample_images'
    ALL_EXCEL         =   'all_excel'
