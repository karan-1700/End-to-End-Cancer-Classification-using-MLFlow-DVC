# component in : src/CNN_Classifier/components

import os
import zipfile
import gdown
from CNN_Classifier import logger
from CNN_Classifier.utils.common import get_size
from CNN_Classifier.config.configuration import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self) -> str:
        '''
        Fetch data from the url
        '''

        try:
            dataset_url = self.config.source_URL
            zip_dataset_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Doanloading data from {dataset_url} into file {zip_dataset_dir}.")

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(url=prefix+file_id, output=zip_dataset_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_dataset_dir}.")

        except Exception as e:
            raise e

    def extract_zip_file(self):
        '''
        reads config.zip_file_path: str
        Extracts the zip file into the data directory.
        Function returns None
        '''
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)


