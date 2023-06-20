import os
import sys # provides access to system-specific parameters and functions
import logging


# sets the logging_str variable to a string format specifying the desired log format. It contains placeholders (such as %(asctime)s, %(levelname)s, etc.) that will be replaced with actual log information when logging messages are created
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


# set the log_dir variable to the directory name where the log files will be stored.
log_dir = "logs"


# creates the log_filepath variable by joining the log_dir and the log file name ("running_logs.log") using the os.path.join() function
log_filepath = os.path.join(log_dir,"running_logs.log")

# creates the log directory specified by log_dir using os.makedirs()
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig( # set up the basic configuration for the logging system
    level= logging.INFO, # set the logging level to INFO, which means that only log messages with the level INFO and above will be recorded
    format= logging_str, # set the log format for the logging messages

    handlers=[
        logging.FileHandler(log_filepath), # FileHandler to write log messages to the log file specified by log_filepath
        logging.StreamHandler(sys.stdout) # write log messages to the standard output (console).
    ]
)


# creates a logger object named "cnnClassifierLogger" using the getLogger() function from the logging module. This logger will be used to log messages throughout the code
logger = logging.getLogger("cnnClassifierLogger")
