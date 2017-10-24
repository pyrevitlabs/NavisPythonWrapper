import sys

from npw.utils.logger import logger

import clr

clr.AddReference('System')                 # Enum, Diagnostics
clr.AddReference('System.Collections')     # List

# Core Imports
from System import Enum
from System.Collections.Generic import List
from System.Diagnostics import Process
