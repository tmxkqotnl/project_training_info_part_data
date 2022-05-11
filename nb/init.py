import sys
from os.path import dirname, realpath, join

parent_dir = dirname(dirname(realpath(__file__)))
sys.path.append(parent_dir)
sys.path.append(join(parent_dir, "Class"))
sys.path.append(join(parent_dir, "controller"))
