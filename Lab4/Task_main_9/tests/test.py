import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab4.Task_main_9.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)



if __name__ == "__main__":
    unittest.main()