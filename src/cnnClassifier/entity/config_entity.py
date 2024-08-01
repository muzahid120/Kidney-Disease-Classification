from pathlib import Path

class DataIngestionConfig:
    def __init__(self, root_dir, source_url, local_data_file, unzip_dir, credentials_info, main_folder_id):
        self.root_dir = root_dir
        self.source_url = source_url
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir
        self.credentials_info = credentials_info
        self.main_folder_id = main_folder_id
