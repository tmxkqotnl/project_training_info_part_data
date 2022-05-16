import logging
import sys
from os.path import dirname, realpath, join

from dotenv import load_dotenv

cur_dir = dirname(realpath(__file__))
parent_dir = dirname(dirname(realpath(__file__)))

sys.path.append(parent_dir.replace("C:", "c:"))
sys.path.append(join(parent_dir, "Class"))
sys.path.append(join(parent_dir, "controller"))

load_dotenv(dotenv_path="../.env", verbose=True)

from os import getenv
from const import LOGGING_LEVEL

logging.basicConfig(
    filename="logs.log",
    encoding="utf-8",
    level=LOGGING_LEVEL[getenv('ENVIROMENT')],
    filemode="a",
    format="%(asctime)s:%(module)s:%(levelname)s -  %(message)s",
)