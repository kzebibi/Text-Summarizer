from src.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from src.logger import logging


def run_data_ingestion_pipeline():
    """
    This function runs the data ingestion pipeline.


    Raises:
    Exception: If any error occurs during the execution of the pipeline.
    """
    STAGE_NAME = "DATA_INGESTION_PIPELINE"
    try:
        logging.info(f"Starting {STAGE_NAME}")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.run()
        logging.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logging.error(f"Error in {STAGE_NAME}")
        logging.error(e)
        raise e


def run_data_validation_pipeline():
    """
    This function runs the data validation pipeline.


    Raises:
    Exception: If any error occurs during the execution of the pipeline.
    """
    STAGE_NAME = "DATA_VALIDATION_PIPELINE"
    try:
        logging.info(f"Starting {STAGE_NAME}")
        data_validation_pipeline = DataValidationTrainingPipeline()
        data_validation_pipeline.run()
        logging.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logging.error(f"Error in {STAGE_NAME}")
        logging.error(e)
        raise e


def run_data_transformation_pipeline():
    """
    This function runs the data transformation pipeline.


    Raises:
    Exception: If any error occurs during the execution of the pipeline.
    """
    STAGE_NAME = "DATA_TRANSFORMATION_PIPELINE"
    try:
        logging.info(f"Starting {STAGE_NAME}")
        data_transformation_pipeline = DataTransformationTrainingPipeline()
        data_transformation_pipeline.run()
        logging.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logging.error(f"Error in {STAGE_NAME}")
        logging.error(e)
        raise e


def run_model_trainer_pipeline():
    """
    This function runs the model trainer pipeline.


    Raises:
    Exception: If any error occurs during the execution of the pipeline.
    """
    STAGE_NAME = "MODEL_TRAINER_PIPELINE"
    try:
        logging.info(f"Running {STAGE_NAME}")
        model_trainer_pipeline = ModelTrainerPipeline()
        model_trainer_pipeline.run()
        logging.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logging.error(f"Error in {STAGE_NAME}")
        logging.error(e)
        raise e


def run_model_evaluation_pipeline():
    """
    This function runs the model evaluation pipeline.


    Raises:
    Exception: If any error occurs during the execution of the pipeline.
    """
    STAGE_NAME = "MODEL_EVALUATION_PIPELINE"
    try:
        logging.info(f"Running {STAGE_NAME}")
        model_evaluation_pipeline = ModelEvaluationPipeline()
        model_evaluation_pipeline.run()
        logging.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logging.error(f"Error in {STAGE_NAME}")
        logging.error(e)
        raise e
