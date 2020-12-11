import itertools
s = []
with open("tmp.txt","r") as i:
	s = i.read()
s = s.strip()


def print_layout(layout):
	print("----------------------------------------------")
	for line in layout:
		print("".join(line))
	print("----------------------------------------------")


# Part 1
def count_neighbors(x,y,layout):
	nrows = len(layout)
	ncolumns = len(layout[0])
	count = 0
	xmin = max(x-1,0)
	ymin = max(y-1,0)
	xmax = min(x+1,nrows-1)
	ymax = min(y+1,ncolumns-1)
	for u in range(xmin,xmax+1):
		for v in range(ymin,ymax+1):
			if (u,v)!=(x,y) and layout[u][v]=="#":
				count+=1
	return count


layout = [[_ if _!="L" else "#" for _ in line] for line in s.split("\n")]
nrows = len(layout)
ncolumns = len(layout[0])

print_layout(layout)
different = True
while different:
	different = False
	new_layout = [[_ for _ in line] for line in layout]
	for x in range(nrows):
		for y in range(ncolumns):
			if count_neighbors(x,y,layout)==0 and layout[x][y]=="L":
				new_layout[x][y] = "#"
				different = True
			elif count_neighbors(x,y,layout)>3 and layout[x][y]=="#":
				new_layout[x][y] = "L"
				different = True
	print_layout(new_layout)
	layout = new_layout
count = sum([sum([1 if _=="#" else 0 for _ in line]) for line in layout])
print(count)

# Part 2
def count_far_neighbors(x,y,layout):
	nrows = len(layout)
	ncolumns = len(layout[0])

	row = layout[x]
	column = [_[y] for _ in layout]

	count = 0
	for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			for size in range(1,max(nrows,ncolumns)):
				if 0<=(x+size*dx)<nrows and 0<=(y+size*dy)<ncolumns and (dx!=0 or dy!=0):
					if layout[x+size*dx][y+size*dy]=="#":
						count+=1
					if layout[x+size*dx][y+size*dy] in ["#","L"]:
						break
				else:
					break
	return count

layout = [[_ if _!="L" else "#" for _ in line] for line in s.split("\n")]
nrows = len(layout)
ncolumns = len(layout[0])

print_layout(layout)
different = True
while different:
	different = False
	new_layout = [[_ for _ in line] for line in layout]
	for x in range(nrows):
		for y in range(ncolumns):
			if count_far_neighbors(x,y,layout)==0 and layout[x][y]=="L":
				new_layout[x][y] = "#"
				different = True
			elif count_far_neighbors(x,y,layout)>4 and layout[x][y]=="#":
				new_layout[x][y] = "L"
				different = True
	print_layout(new_layout)
	layout = new_layout
count = sum([sum([1 if _=="#" else 0 for _ in line]) for line in layout])
print(count)