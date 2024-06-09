from src.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.pipeline.model_evaluation_pipeline import ModelEvaluation
from src.logger import logging



STAGE_NAME = 'DATA_INGESTION_PIPELINE'
try:
    logging.info(f'Starting {STAGE_NAME}')
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.run()
    logging.info(f'Completed {STAGE_NAME}')

except Exception as e:
    logging.error(f'Error in {STAGE_NAME}')
    logging.error(e)
    raise e


STAGE_NAME = 'DATA_VALIDATION_PIPELINE'
try:
    logging.info(f'Starting {STAGE_NAME}')
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.run()
    logging.info(f'Completed {STAGE_NAME}')
except Exception as e:
    logging.error(f'Error in {STAGE_NAME}')
    logging.error(e)
    raise e


STAGE_NAME = 'DATA_TRANSFORMATION_PIPELINE'
try:
    logging.info(f'Starting {STAGE_NAME}')
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.run()
    logging.info(f'Completed {STAGE_NAME}')
except Exception as e:
    logging.error(f'Error in {STAGE_NAME}')
    logging.error(e)
    raise e



STAGE_NAME = "MODEL_TRAINER_PIPELINE"
try:
    logging.info(f'Running {STAGE_NAME}')
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.run()
    logging.info(f'Completed {STAGE_NAME}')
except Exception as e:
    logging.error(f'Error in {STAGE_NAME}')
    logging.error(e)
    raise e
    
STAGE_NAME = "MODEL_TRAINER_PIPELINE"
try:
    logging.info(f'Running {STAGE_NAME}')
    model_trainer_pipeline = ModelEvaluattionPipeline()
    model_trainer_pipeline.run()
    logging.info(f'Completed {STAGE_NAME}')
except Exception as e:
    logging.error(f'Error in {STAGE_NAME}')
    logging.error(e)
    raise e