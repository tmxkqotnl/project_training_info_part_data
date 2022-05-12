import logging
import sys
from os.path import dirname, realpath, join

from dotenv import load_dotenv

parent_dir = dirname(dirname(realpath(__file__)))

sys.path.append(parent_dir.replace("C:", "c:"))
sys.path.append(join(parent_dir, "Class"))
sys.path.append(join(parent_dir, "controller"))

logging.basicConfig(
    filename="logs.log", encoding="utf-8", level=logging.DEBUG, filemode="a"
)
load_dotenv(dotenv_path="./.env", verbose=True)

