from src.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.logger import logging





class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    
    def run(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise e