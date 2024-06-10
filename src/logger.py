import os
import sys
import logging

# Define the logging format string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory for log files
log_dir = "logs"

# Construct the full path to the log file
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it does not exist
os.makedirs(log_dir, exist_ok=True)

# Set the logging level
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        # Log to a file
        logging.FileHandler(log_filepath),
        # Log to the console
        logging.StreamHandler(sys.stdout),
    ],
)
# Get a logger with the specified name
logging = logging.getLogger("textSummarizerLogger")
