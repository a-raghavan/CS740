""" Delete and remake bucket "cs740"
"""

import os
os.system("~/uplink rb sj://cs740 --force")
os.system("~/uplink mb sj://cs740")