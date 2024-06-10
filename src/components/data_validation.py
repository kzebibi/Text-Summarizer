import os
from src.logger import logging
from src.configuration import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
    """
    Initialize a DataValidation object with the provided configuration.

    Args:
    config (DataValidationConfig): The configuration object containing necessary parameters for data validation.

    Returns:
    None
    """
    self.config = config

    def validate_all_files_exist(self) -> bool:
    """
    Validates if all required files exist in the specified directory.

    This method iterates through all files in the directory specified by the
    `ALL_REQUIRED_FILES` attribute of the `config` object. It checks if each file
    is present in the directory. If a file is missing, it writes 'validation_status: False'
    to the file specified by the `STATUS_FILE` attribute of the `config` object and returns False.
    If all files are present, it writes 'validation_status: True' to the status file and returns True.

    Args:
    self (DataValidation): The instance of the DataValidation class.

    Returns:
    bool: True if all required files exist, False otherwise.

    Raises:
    Exception: If any error occurs during the file operations.
    """
    try:
        validation_status = None
        all_files = os.listdir(
            os.path.join("artifacts", "data_ingestion", "samsum_dataset")
        )

        for file in all_files:
            if file not in self.config.ALL_REQUIRED_FILES:
                validation_status = False
                with open(self.config.STATUS_FILE, "w") as f:
                    f.write(f"validation_status: {validation_status}")
            else:
                validation_status = True
                with open(self.config.STATUS_FILE, "w") as f:
                    f.write(f"validation_status: {validation_status}")

        return validation_status
    except Exception as e:
        raise e
