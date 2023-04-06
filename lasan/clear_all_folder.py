from appconfig import AppConfig
import os
import shutil

for file in os.listdir(AppConfig.UPLOAD_FOLDER):
    if(file != '.gitkeep'):
        shutil.rmtree(os.path.join(AppConfig.UPLOAD_FOLDER, file))

for file in os.listdir(AppConfig.OUTPUT_PATH):
    if(file != '.gitkeep'):
        shutil.rmtree(os.path.join(AppConfig.OUTPUT_PATH, file))

for file in os.listdir(AppConfig.FINAL_PATH):
    if(file != '.gitkeep'):
        shutil.rmtree(os.path.join(AppConfig.FINAL_PATH, file))

for file in os.listdir(AppConfig.EXCEL_FILES):
    if(file != '.gitkeep'):
        shutil.rmtree(os.path.join(AppConfig.EXCEL_FILES, file))

for file in os.listdir(AppConfig.TEMP_DIR):
    if(file != '.gitkeep'):
        shutil.rmtree(os.path.join(AppConfig.TEMP_DIR, file))

for file in os.listdir(AppConfig.SAMPLE_IMAGE):
    if(file != '.gitkeep'):
        shutil.rmtree(os.path.join(AppConfig.SAMPLE_IMAGE, file))

for file in os.listdir(AppConfig.ALL_EXCEL):
    if(file != '.gitkeep'):
        os.remove(os.path.join(AppConfig.ALL_EXCEL, file))

