from dataclasses import dataclass
from pathlib import Path


# define the entities
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
    
    
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list
    
    
    
@dataclass(frozen=True)
class DataTransfomationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path
    
    
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    overwrite_output_dir: bool
    num_train_epochs: int # Number of training epochs
    per_device_train_batch_size: int  # Batch size per training GPU/TPU
    save_steps: int   # Save model checkpoint every N steps
    save_total_limit: int  # Maximum number of checkpoints to save
    logging_steps: int # Log training information every N steps
    evaluation_strategy: str  # Evaluate model performance after each epoch
    metric_for_best_model: str  # Metric to monitor for early stopping (minimize loss)
    load_best_model_at_end: bool  # Load the best model based on the monitored metric
    warmup_steps: int  # Number of warmup steps for learning rate scheduler
    learning_rate: float  # Learning rate for the optimizer
    adam_epsilon: float  # Epsilon for Adam optimizer
    weight_decay: float  # Weight decay for optimizer


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path