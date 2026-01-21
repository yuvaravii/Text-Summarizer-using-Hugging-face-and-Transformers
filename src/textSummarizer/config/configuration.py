# since we got the input and output director, we need to read the yaml and store them as value
from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import read_yaml, create_directories
from src.textSummarizer.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,      # loading from constants
                 params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # creating artifacts folder/ parent output folder
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion  # reading all the necessary file within the config.yaml/data_ingestion
        create_directories([config.root_dir])  # creating the parent directory for data_ingestion component

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL=  config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir,
        )
        return data_ingestion_config