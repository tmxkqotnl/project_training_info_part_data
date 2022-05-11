import sys
from os.path import dirname, realpath

parent_dir = dirname(realpath(__file__))
sys.path.append(parent_dir)

from training_list_controller import *
from url_controller import *
