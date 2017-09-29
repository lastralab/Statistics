# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Tania M. Molina
# UY - 2017
# MIT License
import math
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import norm
import scipy.stats as stats
import scipy.stats as st
import matplotlib
import matplotlib.pyplot as plt
import re
import scipy.stats
import matplotlib.pyplot as mlab

fhand = raw_input('Enter .csv file name or keyword: ')

data = pd.read_csv(fhand, header=0)

frame = pd.DataFrame(data)
