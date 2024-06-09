from src.constants import *
from src.utils import read_yaml, create_directories
from src.entity import (DataIngestionConfig,
                        DataValidationConfig,
                        DataTransfomationConfig,
                        ModelTrainerConfig,
                        ModelEvaluationConfig)




class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH):
    
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self):
        config = self.config.data_ingestion
        create_directories([config.root_dir])
    
        data_ingestion_config = DataIngestionConfig(
                                root_dir = config.root_dir,
                                source_URL = config.source_URL,
                                local_data_file = config.local_data_file,
                                unzip_dir = config.unzip_dir,
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,

        )

        return data_validation_config



    def get_data_transformation_config(self) -> DataTransfomationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config = DataTransfomationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            tokenizer_name = config.tokenizer_name,
        )
        return data_transformation_config
    
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingArguments
        create_directories([config.root_dir])
        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            model_ckpt = config.model_ckpt,
            overwrite_output_dir = config.overwrite_output_dir,
            num_train_epochs = params.num_train_epochs,
            per_device_train_batch_size= config.per_device_train_batch_size,
            save_steps = config.save_steps,
            save_total_limit = config.save_total_limit,
            logging_steps = config.logging_steps,
            evaluation_strategy = config.evaluation_strategy,
            metric_for_best_model = config.metric_for_best_model,
            load_best_model_at_end = config.load_best_model_at_end,
            warmup_steps = config.warmup_steps,
            learning_rate = config.learning_rate,
            adam_epsilon = config.adam_epsilon,
            weight_decay = config.weight_decay
        )
        
        return model_trainer_config

    
    
    def get_model_evaluation_config(self):
        config = self.config.model_evaluation
        
        create_directories([config.root_dir])
        
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path=config.model_path,
            tokenizer_path=config.tokenizer_path,
            metric_file_name= config.metric_file_name
        )
        
        return model_evaluation_config