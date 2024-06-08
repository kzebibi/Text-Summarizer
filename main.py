from src.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.logger import logging



# STAGE_NAME = 'DATA_INGESTION_PIPELINE'
# try:
#     logging.info(f'Starting {STAGE_NAME}')
#     data_ingestion_pipeline = DataIngestionTrainingPipelinee()
#     data_ingestion_pipeline.run()
#     logging.info(f'Completed {STAGE_NAME}')

# except Exception as e:
#     logging.error(f'Error in {STAGE_NAME}')
#     logging.error(e)
#     raise e


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
