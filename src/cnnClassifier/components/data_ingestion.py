from src.cnnClassifier._m_logging import logging
from src.cnnClassifier.my_exception import CustomException
from src.cnnClassifier.entity.config_entity import DataIngestionConfig
import os 
from dataclasses import dataclass
from urllib.request import Request
import zipfile
from pathlib import Path


@dataclass(frozen=True)
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):

        self.config=config
