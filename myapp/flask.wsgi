import sys
import os
DIR=os.path.dirname(__file__)
sys.path.append(DIR)
sys.path.insert(0, '/home/s2022072/myapp/')
from myapp import app as application