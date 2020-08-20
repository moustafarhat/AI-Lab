# Example of the Shapiro-Wilk Normality Test
'''
Tests whether a data sample has a Gaussian distribution.
Assumptions
Observations in each sample are independent and identically distributed (iid).
Interpretation
H0: the sample has a Gaussian distribution.
H1: the sample does not have a Gaussian distribution.
'''

from scipy.stats import shapiro
data = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869,10]
stat, p = shapiro(data)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')
 
 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

sns.set(color_codes=True)

sns.distplot(data);
plt.show()