# import necessary packages
import os
import sys
import logging

# logging_str = "[%(asctime)s] [%(levelname)s] [%(module)s] : %(message)s"
logging_str = "[%(asctime)s] [%(levelname)s] [%(module)s.%(funcName)s:%(lineno)d] [%(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log") # save logs to a file
# create log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath), # save logs to a file
        logging.StreamHandler(sys.stdout) # also print logs to console/terminal
    ]
)

logger = logging.getLogger("CNN_Classifier_Logger")
