import math

s = []
with open("tmp.txt","r") as i:
	s = i.read()
s = s.strip()

departure_time = int(s.split('\n')[0])
buses = [int(_) for _ in s.split('\n')[1].split(',') if _ != 'x']

# Part 1
waiting_time = 2*departure_time
earliest_bus = None
for bus in buses:
	wt = (((departure_time//bus)+1)*bus)%departure_time
	if wt < waiting_time:
		waiting_time = wt
		earliest_bus = bus
print(earliest_bus*waiting_time)

# Part 2
buses = [int(_) for _ in s.split('\n')[1].split(',') if _ != 'x']
remainders = [(-index)%int(_) for index,_ in enumerate(s.split('\n')[1].split(',')) if _ != 'x']

timestamp = 0
n = math.prod(buses)
for index in range(len(buses)):
	inv = pow(n//buses[index], -1, buses[index])
	timestamp+=inv*(n//buses[index])*remainders[index]
print(timestamp%n)