from src.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer
from src.logger import logging




class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    
    def run(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(model_trainer_config)
            model_trainer.train()

        except Exception as e:
            raise e