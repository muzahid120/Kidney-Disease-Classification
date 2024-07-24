from src.cnnClassifier.constants import *
from src.cnnClassifier.entity.config_entity import DataIngestionConfig
from src.cnnClassifier.utils.common import read_yaml,create_directories

import os 



class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH):
        
        self.config=config_file_path
        self.params=params_file_path

        read_yaml(self.config,self.params)

        create_directories([self.config.artifacts_root])
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config


        
