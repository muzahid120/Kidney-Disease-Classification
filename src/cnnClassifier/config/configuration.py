import yaml
from pathlib import Path
from src.cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_path):
        self.config = self._load_yaml(config_path)
    
    def _load_yaml(self, path):
        with open(path, 'r') as file:
            return yaml.safe_load(file)

    def get_data_ingestion_config(self):
        config = self.config.get('data_ingestion', {})
        return DataIngestionConfig(
            root_dir=Path(config.get('root_dir')),
            source_url=config.get('source_url'),
            local_data_file=Path(config.get('local_data_file')),
            unzip_dir=Path(config.get('unzip_dir')),
            credentials_info=self.config.get('google_drive', {}).get('credentials_info'),
            main_folder_id=config.get('main_folder_id')
        )
