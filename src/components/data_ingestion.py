from dataclasses import dataclass
from pathlib import Path
from src.constants import *
import os
import urllib.request as request
import zipfile
from src.logger import logging
from src.utils import get_size
from src.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
    """
    Initializes the DataIngestion class with a configuration.

    Args:
    config (DataIngestionConfig): The configuration object that contains all necessary parameters for data ingestion.

    Returns:
    None
    """
    self.config = config

    def download_file(self):
        """
        Downloads the file if it doesn't exist.
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL, filename=self.config.local_data_file
            )
            logging.info(f"{filename} download! with following info: \n{headers}")
        else:
            logging.info(
                f"File already exists of size: {get_size(Path(self.config.local_data_file))}"
            )

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)


if __name__ == "__main__":
    try:
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    except Exception as e:
        raise e
