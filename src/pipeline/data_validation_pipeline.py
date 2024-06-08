from src.configuration import ConfigurationManager
from src.components.data_validation import DataValidation 
from src.logger import logging




class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    
    def run(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_files_exist()

        except Exception as e:
            raise e