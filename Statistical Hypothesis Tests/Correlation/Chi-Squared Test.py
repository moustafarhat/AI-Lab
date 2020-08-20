
'''
Tests whether two categorical variables are related or independent.

Assumptions

    Observations used in the calculation of the contingency table are independent.
    25 or more examples in each cell of the contingency table.

Interpretation

    H0: the two samples are independent.
    H1: there is a dependency between the samples.

'''
	
# Example of the Chi-Squared Test
from scipy.stats import chi2_contingency
table = [[10, 20, 30],[10,  7,  9]]
stat, p, dof, expected = chi2_contingency(table)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably independent')
else:
	print('Probably dependent')