import logging
import os
import sys

# Define the logging format
log_format = "[%(asctime)s] *** %(message)s *** %(levelname)s:%(module)s"

# Directory and file path for the log
log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'running_log.log')

# Ensure the log directory exists
os.makedirs(log_dir, exist_ok=True)

# Configure the logging
logging.basicConfig(
    format=log_format,
    level=logging.INFO,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Optionally, you might want to add a logger instance for specific modules
logger = logging.getLogger()
