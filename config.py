import os
import sys

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

###############
#
#   logger
#
###############

enable_file = True

from datetime import datetime
_timestamp = datetime.now().strftime('%m-%d-%H-%M-%S')
log_dir = os.path.join("log", '-'.join(['log', _timestamp]))

if enable_file:
    os.mkdir(log_dir)