# creating the component
import os
import urllib.request as request
import zipfile 

from src.textSummarizer.logging import logger
from src.textSummarizer.utils.common import *
from src.textSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        input/arguments: DataIngestionConfig class instance
        process: Downloads all the resources mentioned in the url --> unzip --> store in local repository
        output: Downloaded data in the local repo
        """

        if not os.path.exists(self.config.local_data_file):    # create local data file if it does not exist
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"File downloaded and stored in local Successfully!!!")
        else:
            logger.info(f"File already Exists!! ")

    
    def extract_zip_file(self):
        """
        This extracts the zip_file_path into the data directory
        and this returns None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)