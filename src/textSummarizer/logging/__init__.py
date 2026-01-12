import os 
import sys
import logging

log_dir = "logs"
logging_str = "[%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s]"
log_filepath = os.path.join(log_dir,"execution_logs.log")

# creating the logs directory
os.makedirs(log_dir, exist_ok = True)

logging.basicConfig(
    level=logging.INFO,
    format= logging_str,
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_filepath),   # writes all the logs to this specific filepath.
        logging.StreamHandler(sys.stdout)   # writes all the logs in the console where the code is executed.
    ],
    force = True,       # this ensures there is no silent failure happening back the door
)

# now calling the above logger
logger = logging.getLogger("summarizerLogger")