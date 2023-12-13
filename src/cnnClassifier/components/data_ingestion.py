import os
import urllib.request as request
import zipfile
import shutil
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        source_path = self.config.source_file_path  # Specify the source file path
        destination_path = self.config.local_data_file  # Specify the destination file path

        if not os.path.exists(destination_path):
            try:
                shutil.copyfile(source_path, destination_path)
                logger.info(f"File copied from {source_path} to {destination_path}")
            except FileNotFoundError:
                logger.error(f"Source file {source_path} not found.")
        else:
            logger.info(f"File already exists at {destination_path}")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
