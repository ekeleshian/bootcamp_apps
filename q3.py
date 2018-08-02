import csv
from pdb import set_trace

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

def success_ratio(input):
	sr = []
	for i, v in input:
		sr.append(float(i/v))
	print(sr)

success_ratio(baseline)
success_ratio(variations)


