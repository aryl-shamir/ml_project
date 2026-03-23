import logging
import os
from datetime import datetime

# Step 1: create safe log file name
LOG_FILE = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"

# Step 2: create logs folder path
logs_dir = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Step 3: create folder if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Step 4: create full file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Step 5: configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
