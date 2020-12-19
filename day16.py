import re

s = []
with open("tmp.txt","r") as i:
	s = i.read()
s = s.strip()

intervals = []
for interval in re.findall("[0-9]+-[0-9]+",s):
	intervals.append({"min":int(interval.split("-")[0]),"max":int(interval.split("-")[1])})

tickets = [[int(_) for _ in line.split(",")] for line in s.split("nearby tickets:\n")[1].split("\n")]
valid_tickets = []
err_rate = 0
for ticket in tickets:
	valid = True
	for value in ticket:
		if all([interval["min"]>value or interval["max"]<value for interval in intervals]):
			valid = False
			err_rate+=value
	if valid:
		valid_tickets.append(ticket)

print(err_rate)

lines = s.split("\n\n")[0].split("\n")
nb_rules = len(lines)
rules = {lines[_].split(":")[0]:intervals[2*_:2*_+2] for _ in range(nb_rules)}
fields = {_:[] for _ in range(nb_rules)}

def check_rule(place,intervals,tickets):
	return all([any([interval["min"]<=ticket[place]<=interval["max"] for interval in intervals]) for ticket in tickets])

for place in fields:
	for field in rules:
		if check_rule(place,rules[field],valid_tickets):
			fields[place].append(field)

while max([len(_) for _ in fields.values()])>1:
	for place in [_ for _ in fields if len(fields[_])>1]:
		tmp = []
		for field in fields[place]:
			if not any([field in fields[_] and len(fields[_])==1 for _ in fields]):
				tmp.append(field)
		fields[place]=tmp
fields = {_[1][0]:_[0] for _ in fields.items()}

ticket = [int(_) for _ in s.split("\n\nyour ticket:\n")[1].split("\n")[0].split(",")]
output = 1
for field in rules:
	if field.startswith("departure"):
		output*=ticket[fields[field]]
print(output)