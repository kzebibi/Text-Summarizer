from src.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer
from src.logger import logging


class ModelTrainerPipeline:
    """
    This class represents a pipeline for training a machine learning model.
    It initializes the necessary components and orchestrates the training process.
    """

    def __init__(self):
        """
        Initializes an instance of ModelTrainerPipeline.
        No parameters are required for this method.
        """
        pass

    def run(self):
        """
        Runs the model training pipeline.

        This method retrieves the model trainer configuration, initializes the model trainer,
        and then trains the model. If any exception occurs during the process, it is raised.

        Returns:
            None
        """
        try:
            # Retrieve the model trainer configuration
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()

            # Initialize the model trainer
            model_trainer = ModelTrainer(model_trainer_config)

            # Train the model
            model_trainer.train()

        except Exception as e:
            # If an exception occurs, raise it
            raise e