from src.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation
from src.logger import logging


class ModelEvaluationPipeline:
    """
    This class represents a pipeline for evaluating machine learning models.
    """

    def __init__(self):
        """
        Initializes a new instance of ModelEvaluationPipeline.
        """
        pass

    def run(self):
        """
        Runs the model evaluation pipeline.

        This method retrieves the model evaluation configuration from the configuration manager,
        creates a ModelEvaluation object with the configuration, and evaluates the model.

        Raises:
            Exception: If any error occurs during the evaluation process.
        """
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.evaluate()

        except Exception as e:
            raise e