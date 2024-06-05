import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Create the data directory and subdirectories
data_dir = 'data'
raw_dir = os.path.join(data_dir, 'raw')
processed_dir = os.path.join(data_dir, 'processed')
os.makedirs(data_dir, exist_ok=True)
os.makedirs(raw_dir, exist_ok=True)
os.makedirs(processed_dir, exist_ok=True)

# Create the artifacts diractory and subdirectories 
artifacts_dir = 'artifacts'
models_dir = os.path.join(artifacts_dir, 'models')
reports_dir = os.path.join(artifacts_dir, 'reports')
os.makedirs(artifacts_dir, exist_ok=True)
os.makedirs(models_dir, exist_ok=True)
os.makedirs(reports_dir, exist_ok=True)

# Create the other files
list_of_files = [
    # data dir
    "data/README.md",
    # models dir
    "models/model.py",
    "models/utils.py",
    "models/metrics.py",
    "models/hyperparameter_tuning.py",
    "models/README.md",
    # notebooks dir
    "notebooks/00_exploratory.ipynb",
    "notebooks/01_preprocessing.ipynb",
    "notebooks/02_model_training.ipynb",
    "notebooks/03_model_evaluation.ipynb",
    "notebooks/README.md",
    # src dir
    "src/__init__.py",
    "src/components/__init__.py"
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/pipeline/__init__.py",
    "src/exception.py",
    "src/logger.py",
    "src/utils.py",
    # tests dir
    "tests/__init__.py",
    "tests/test_config.py",
    "tests/test_data.py",
    "tests/test_model.py",
    "tests/test_train.py",
    "tests/test_utils.py",
    "tests/preprocessing.py",
    "tests/README.md",
    # scripts dir 
    "scripts/run_training.sh",
    "scripts/run_evaluation.sh",
    "scripts/run_prediction.sh",
    # logs dir 
    "logs/training.log",
    "logs/evaluation.log",
    "logs/prediction.log",
    # other files
    ".github/workflows/.gitkeep",
    "config/config.yaml",
    "dvc.yaml",
    "Dockerfile",
    "docker_compose.yml",
    "app.py",
    "config.py",
    "params.yaml",
    "README.md",
    "requirements.txt",
    "setup.py",
    "research/trial.ipynb",
    "templates/index.html",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File {filepath} already exists")


print("Project structure created successfully!")
