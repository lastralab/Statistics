import numpy as np
from scipy import stats
import pandas as pd
import seaborn as sns
from pydataset import data
import matplotlib.pyplot as plt
import matplotlib.cm as cm

sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})
faithful = data('faithful')
faithful.head(272) #number of lines of data to extract
#histogram:
faithful['eruptions'].hist(bins=8)
plt.xlabel("Minutes")
plt.ylabel("Frequence")
plt.show()
