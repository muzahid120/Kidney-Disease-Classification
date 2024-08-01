import os
import zipfile
from src.cnnClassifier.utils.google_drive_utils import GoogleDriveService
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier._m_logging import logging
from src.cnnClassifier.my_exception import CustomException

class DataIngestion:
    def __init__(self, config: ConfigurationManager):
        self.config = config

    def download_data(self):
        try:
            data_ingestion_config = self.config.get_data_ingestion_config()

            logging.info(f"Data ingestion configuration: {data_ingestion_config}")

            if not data_ingestion_config.credentials_info:
                raise ValueError("Credentials info is missing from data ingestion configuration")

            google_drive_api = GoogleDriveAPI(
                credentials_info=data_ingestion_config.credentials_info,
                folder_id=data_ingestion_config.main_folder_id,
                local_directory=os.path.dirname(data_ingestion_config.local_data_file)
            )

            zip_file_path = google_drive_api.download_zip_file()
            logging.info(f"ZIP file path returned: {zip_file_path}")

            if zip_file_path:
                logging.info(f"ZIP file downloaded successfully: {zip_file_path}")
                # Extract ZIP file is commented out as per requirement
                # self.extract_zip_file(zip_file_path, data_ingestion_config.unzip_dir)
            else:
                logging.error("No ZIP file was downloaded.")
        except Exception as e:
            logging.error(f"An error occurred during data ingestion: {e}")
            raise CustomException("Data ingestion failed", str(e))

    def extract_zip_file(self, zip_file_path, extract_to):
        try:
            if zipfile.is_zipfile(zip_file_path):
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_to)
                os.remove(zip_file_path)  # Remove the zip file after extraction
                logging.info(f"ZIP file extracted successfully to: {extract_to}")
                extracted_files = os.listdir(extract_to)
                logging.info(f"Extracted files: {extracted_files}")
            else:
                logging.error(f"The file {zip_file_path} is not a valid ZIP file.")
                raise ValueError(f"The file {zip_file_path} is not a valid ZIP file.")
        except Exception as e:
            logging.error(f"An error occurred while extracting ZIP file: {e}")
            raise CustomException("Extraction failed", str(e))
