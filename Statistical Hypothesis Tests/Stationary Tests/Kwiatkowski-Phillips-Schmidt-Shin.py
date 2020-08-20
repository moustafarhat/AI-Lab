'''
Tests whether a time series is trend stationary or not.

Assumptions

    Observations in are temporally ordered.

Interpretation

    H0: the time series is not trend-stationary.
    H1: the time series is trend-stationary.

'''

# Example of the Kwiatkowski-Phillips-Schmidt-Shin test
from statsmodels.tsa.stattools import kpss
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
stat, p, lags, crit = kpss(data)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably not Stationary')
else:
	print('Probably Stationary')