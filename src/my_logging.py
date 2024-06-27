import os
from datetime import datetime
import logging

# Create a log file name with the current date and time
log_file = f"{datetime.now().strftime('%d_%m_%H_%M_%S')}.log"

# Create the logs directory path
logs_dir = os.path.join(os.getcwd(), 'logs')

# Make sure the logs directory exists
os.makedirs(logs_dir, exist_ok=True)

# Create the full path for the log file
log_file_path = os.path.join(logs_dir, log_file)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s]**%(lineno)d**%(levelname)s**%(name)s**%(message)s",
    level=logging.INFO,
)

# Example usage
logging.info("This is an informational message.")
logging.error("This is an error message.")
