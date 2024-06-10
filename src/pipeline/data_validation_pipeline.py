from src.configuration import ConfigurationManager
from src.components.data_validation import DataValidation 
from src.logger import logging


class DataValidationTrainingPipeline:
    """
    This class represents a pipeline for training data validation.
    It initializes a ConfigurationManager, retrieves data validation configuration,
    and validates all required files exist.
    """

    def __init__(self):
        """
        Initializes an instance of DataValidationTrainingPipeline.
        No parameters are required.
        """
        pass

    
    def run(self):
        """
        Runs the data validation training pipeline.

        Retrieves the data validation configuration, creates a DataValidation instance,
        and validates all required files exist.

        Raises:
            Exception: If any error occurs during the process.
        """
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_files_exist()

        except Exception as e:
            raise e