import re
s = []
with open("tmp.txt","r") as i:
	s = i.readlines()
boardings = [_.strip() for _ in s]
boardings = [{"row":boarding[0:7],"column":boarding[7:]} for boarding in boardings]

# Part 1
max_id = 0
boarding_ids = []
for boarding in boardings:
	row = int(boarding["row"].replace("F","0").replace("B","1"),2)
	column = int(boarding["column"].replace("L","0").replace("R","1"),2)
	ID = 8*row+column
	boarding_ids.append(ID)
	if ID>max_id:
		max_id = ID
print("Highest ID")
print(max_id)

# Part 2
for i in range(1,max_id):
	if {i-1,i+1}.issubset(set(boarding_ids)) and i not in boarding_ids:
		print("Potential seat")
		print(i)