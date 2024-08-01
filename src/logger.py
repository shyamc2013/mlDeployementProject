import logging
import os
from datetime import datetime

# strftime() method returns a string representing date and time
LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# join all the 3 strs using a / between them
logs_path= os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(logs_path, exist_ok= True)

LOG_FILE_PATH= os.path.join(logs_path, LOG_FILE)

# %(asctime)s: This will be replaced by the timestamp of the log message.
# %(lineno)d: line number in the source code where the log message was generated.
# %(name)s: name of the logger that generated the log message.
# %(levelname)s: log level name (e.g., INFO, DEBUG, ERROR).
# %(message)s: actual log message.

# logging.INFO: This sets the logging level to INFO. It means that only log messages with a severity level of INFO or higher (e.g., WARNING, ERROR, CRITICAL) will be captured and written to the log file. DEBUG messages, which have a lower severity level than INFO, will be ignored.

# sets up the basic configuration for the logging system, including the log file, format, and log level.
logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= '[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level= logging.INFO
)
