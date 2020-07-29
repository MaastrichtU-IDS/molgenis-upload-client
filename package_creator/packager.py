import os
import zipfile
from logger.logger import log

def create_package(path, zipfile_name):
    log.info("Creating package for path: %s, zip name: %s.", path, zipfile_name)
    zip = zipfile.ZipFile(zipfile_name, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))
    zip.close()