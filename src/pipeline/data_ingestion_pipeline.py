from src.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.logger import logging


class DataIngestionTrainingPipeline:
    """
    This class represents a data ingestion training pipeline.
    It handles the process of downloading and extracting data for training.
    """

    def __init__(self):
        """
        Initializes a new instance of DataIngestionTrainingPipeline.
        """
        pass

    def run(self):
        """
        Runs the data ingestion training pipeline.

        This method performs the following steps:
        1. Retrieves the data ingestion configuration using ConfigurationManager.
        2. Creates a new instance of DataIngestion with the retrieved configuration.
        3. Downloads the data file using the DataIngestion instance.
        4. Extracts the downloaded zip file using the DataIngestion instance.

        If any exception occurs during the process, it is re-raised.
        """
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e