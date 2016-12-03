#!/usr/bin/python

import argparse
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# get month 
parser = argparse.ArgumentParser(description='search for month')
parser.add_argument("months", help="month")
args = parser.parse_args()

