import csv
path = 'data.csv'

x = []
y = []

with open(path, newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		x.append(row[1])
		y.append(row[2])
print(x)
print(y)
		
baseline = (x[1], y[1])

variations = [(x[2], y[2]),(x[3], y[3]), (x[4],y[4]), (x[5], y[5])]

