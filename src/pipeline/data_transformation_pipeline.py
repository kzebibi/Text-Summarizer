from src.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.logger import logging



class DataTransformationTrainingPipeline:
    """
    This class represents a pipeline for training data transformation.
    """

    def __init__(self):
        """
        Initialize an instance of DataTransformationTrainingPipeline.
        """
        pass

    
    def run(self):
        """
        Run the data transformation training pipeline.

        This method retrieves the data transformation configuration, creates an instance of DataTransformation,
        and calls the convert method to perform the transformation.

        Raises:
            Exception: If any error occurs during the process.
        """
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise e