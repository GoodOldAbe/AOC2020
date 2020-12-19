import itertools
import operator

s = []
with open("tmp.txt","r") as i:
	s = i.read()
s = s.strip()

nrows = len(s.split("\n"))
ncols = len(s.split("\n")[0])


def count_active_neighbors(position,layout,nb_dimensions):
	nb_act = 0
	for delta in list(itertools.product([-1,0,1],repeat=nb_dimensions)):
		if delta != tuple(0 for _ in range(nb_dimensions)):
			neighbor = tuple(map(operator.add, position, delta))
			if neighbor in layout and layout[neighbor]=="#":
				nb_act+=1
	return nb_act


def get_all_positions(layout,nb_dimensions):
	positions = []
	for position in layout:
		if layout[position]=="#":
			for delta in list(itertools.product([-1,0,1],repeat=nb_dimensions)):
				neighbor = tuple(map(operator.add, position, delta))
				if neighbor not in positions:
					positions.append(neighbor)
	return positions


def run_cycle(layout,nb_dimensions):
	new_layout = {}
	for position in get_all_positions(layout,nb_dimensions):
		nb_act = count_active_neighbors(position,layout,nb_dimensions)
		if position not in layout:
			if nb_act==3:
				new_layout[position]="#"
		else:
			if (layout[position]=="#" and nb_act in [2,3]) or (layout[position]=="." and nb_act==3):
				new_layout[position]="#"
			else:
				new_layout[position]="."
	return new_layout

# Part 1
layout = {}
for x in range(nrows):
	for y in range(ncols):
		layout[(x,y,0)]=s.split("\n")[x][y]

for cycle in range(6):
	layout = run_cycle(layout,3)

print(sum([1 if layout[position]=="#" else 0 for position in layout]))

# Part 2
layout = {}
for x in range(nrows):
	for y in range(ncols):
		layout[(x,y,0,0)]=s.split("\n")[x][y]

for cycle in range(6):
	print("Running cycle {}".format(cycle))
	layout = run_cycle(layout,4)

print(sum([1 if layout[position]=="#" else 0 for position in layout]))