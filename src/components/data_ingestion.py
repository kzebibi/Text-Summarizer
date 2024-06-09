from dataclasses import dataclass
from pathlib import Path
from src.constants import *
import os
import urllib.request as request
import zipfile
from src.logger import logging
from src.utils import read_yaml, create_directories, get_size
from src.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
        self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH
    ):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self):
        """
        Retrieves the data ingestion configuration.
        """
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )
        return data_ingestion_config


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        Initializes the DataIngestion class with a configuration.
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
