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
    num_train_epochs: int
    per_device_train_batch_size: int
    save_steps: int
    save_total_limit: int
    logging_steps: int
    evaluation_strategy: str
    metric_for_best_model: str
    load_best_model_at_end: bool
    warmup_steps: int
    learning_rate: float
    adam_epsilon: float
    weight_decay: float


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path
