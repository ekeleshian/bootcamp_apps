import csv
from pdb import set_trace
import numpy as np
import scipy.stats
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import figure_factory as ff
from plotly.offline import iplot


path = 'data.csv'

x = []
y = []

with open(path, newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		x.append(row[1])
		y.append(row[2])
# print(x)
# print(y)
		
baseline = [(int(x[1]), int(y[1]))]

variations = [(int(x[2]), int(y[2])),(int(x[3]), int(y[3])),(int(x[4]),int(y[4])), (int(x[5]), int(y[5]))]
# print(baseline, variations)

'''Success ratio (i.e. the SR) is the ratio in which providers 
actually follow up with requests and send a quote.
If we want more providers to respond to requests, 
we need to maximize the success ratio'''
def success_ratio(input):
	sr = []
	for i, v in input:
		sr.append(float(i/v))
	return sr

'''Let's assume that the SR of the baseline is what we normally
expect, i.e. without any variations, this is the SR we obtain 
on average. Because of this, let's further assume that the SR of
the baseline is the expected value, i.e. the average of SR results with
out doing any experimentation'''

expected_value = success_ratio(baseline)

'''Let's now assume that the variations were conducted without any influence
from each other.  In other words, each variation is an independent event. '''

variation_set = success_ratio(variations)

'''Let's break down what we have set up so far:
1.  The expected value
2.  A dataset that contains events that are independent from each other
3.  A very small set of samples (only 4 SR's are obtained to compare them with 1 SR)

Due to the nature of this set-up, what's most appropriate is to conduct a One
Sample T-test. A One Sample T-test allows us to work with small sample sizes to determine whether the
manipulations that were made in the variation set are, on average, statistically 
significant from the expected value. In other words, do the variations actually
generate results that are sufficient enough to make changes in the information flow
between the customer and provider.

So, let's build a null and alternate hypothesis:
Null Hypothesis:  Variations do not impact the SR
Alternate Hypothesis:  Variations significantly impact the SR

At this point, we can start coding.'''

# Let's make our alpha 0.05.  This means, we are 100% - alpha = 95% confident 
# that our test is valid

# Let us also calculate the degree of freedom here: 1 + 4 - 2 = 3

onesample_results = scipy.stats.ttest_1samp(variation_set, expected_value[0])


print(onesample_results)
# matrix_onesample = [['', 'Test Statistic', 'p-value'], ['Sample Data', 
# onesample_results[0], onesample_results[1]]]

# onesample_table = ff.create_table(matrix_onesample, index = True)
# #set_trace()
# py.iplot(onesample_table, filename='onesample-table')




