from box.exceptions import BoxValueError
import os 
import yaml
from src.logger import logging
from box import ConfigBox
from pathlib import Path
from typing import Any
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return a ConfigBox object.
    
    Args:
    path_to_yaml (Path): Path to the YAML file.
    
    Raises:
    BoxValueError: If the YAML file does not exist or cannot be read.
    
    Returns:
    ConfigBox: A ConfigBox object containing the contents of the YAML file.
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
    
@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file or directory.
    
    Args:
    path (Path): Path to the file or directory.
    
    Returns:
    str: The size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"` {size_in_kb} KB"


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories if they do not exist.
    
    Args:
        path_to_directories (list): List of paths to directories.
        verbose (bool, optional): If True, log the creation of each directory. Defaults to True.
        
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Created directory at: {path}")