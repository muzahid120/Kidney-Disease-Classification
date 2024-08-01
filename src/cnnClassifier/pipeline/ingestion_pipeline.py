from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self, config_path):
        self.config_manager = ConfigurationManager(config_path)
        self.data_ingestion_config = self.config_manager.get_data_ingestion_config()
        self.data_ingestion = DataIngestion(self.data_ingestion_config)
    
    def run(self):
        print("Starting data ingestion pipeline...")
        all_pictures = self.data_ingestion.download_data()
        self._print_results(all_pictures)
    
    def _print_results(self, pictures):
        for picture in pictures:
            print(f"ID: {picture['id']}, Name: {picture['name']}")

if __name__ == '__main__':
    pipeline = DataIngestionPipeline(r'C:\Users\SDS\kidney-disease-classification\config\config.yaml')
    pipeline.run()
