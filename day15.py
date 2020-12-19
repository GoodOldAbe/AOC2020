import math

s = []
with open("tmp.txt","r") as i:
	s = i.read()
s = s.strip()

# Part 1
series = [int(_) for _ in s.split(",")]
while len(series)<2020:
	if series[-1] not in series[:-1]:
		series.append(0)
	else:
		for index in range(2,len(series)+1):
			if series[len(series)-index]==series[-1]:
				series.append(index-1)
				break
print(series[-1])

# Part 2
series = [int(_) for _ in s.split(",")]
counter = {series[_]:_+1 for _ in range(len(series))}
current = series[-1]
age = len(series)
next = 0
while age<30000000:
	age+=1
	current = next
	if current in counter:
		next = age-counter[current]
	else:
		next=0
	counter[current] = age
print(current)
