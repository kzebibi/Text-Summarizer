from dataclasses import dataclass
from pathlib import Path


# define the entities

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration for data ingestion process.

    Attributes:
    root_dir (Path): Root directory for data.
    source_URL (str): URL from where to download data.
    local_data_file (Path): Local path to save downloaded data.
    unzip_dir (Path): Directory to unzip downloaded data.
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    """
    Configuration for data validation process.

    Attributes:
    root_dir (Path): Root directory for data.
    STATUS_FILE (str): File name to store validation status.
    ALL_REQUIRED_FILES (list): List of all required files for validation.
    """
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list


@dataclass(frozen=True)
class DataTransfomationConfig:
    """
    Configuration for data transformation process.

    Attributes:
    root_dir (Path): Root directory for data.
    data_path (Path): Path to the data to be transformed.
    tokenizer_name (Path): Path to the tokenizer to be used for transformation.
    """
    root_dir: Path
    data_path: Path
    tokenizer_name: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    """
    Configuration for model training process.

    Attributes:
    root_dir (Path): Root directory for data and models.
    data_path (Path): Path to the training data.
    model_ckpt (Path): Path to the pre-trained model checkpoint.
    overwrite_output_dir (bool): Whether to overwrite the output directory.
    num_train_epochs (int): Number of training epochs.
    per_device_train_batch_size (int): Batch size per device during training.
    save_steps (int): Steps to save the model.
    save_total_limit (int): Maximum total number of checkpoints to save.
    logging_steps (int): Steps to log training progress.
    evaluation_strategy (str): Evaluation strategy during training.
    metric_for_best_model (str): Metric to use for selecting the best model.
    load_best_model_at_end (bool): Whether to load the best model at the end.
    warmup_steps (int): Steps for warmup during training.
    learning_rate (float): Learning rate for training.
    adam_epsilon (float): Adam epsilon value.
    weight_decay (float): Weight decay for training.
    """
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
    """
    Configuration for model evaluation process.

    Attributes:
    root_dir (Path): Root directory for data and models.
    data_path (Path): Path to the evaluation data.
    model_path (Path): Path to the trained model.
    tokenizer_path (Path): Path to the tokenizer used for evaluation.
    metric_file_name (Path): File name to store evaluation metrics.
    """
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path