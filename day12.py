import numpy as np
s = []
with open("tmp.txt","r") as i:
	s = i.read()
s = s.strip()


instructions = [{"opcode":_[0],"value":int(_[1:])} for _ in s.split("\n")]
translations = {"N":np.array([0,1]),"S":np.array([0,-1]), "E":np.array([1,0]), "W":np.array([-1,0])}
orientations = [np.array([1,0]),np.array([0,1]),np.array([-1,0]),np.array([0,-1])]

# Part 1
position = np.array([0,0])
o_index = 0
for instruction in instructions:
	if instruction["opcode"] in ["N","S","E","W"]:
		position = position+translations[instruction["opcode"]]*instruction["value"]
	elif instruction["opcode"] == "L":
		o_index = (o_index+instruction["value"]//90)%4
	elif instruction["opcode"] == "R":
		o_index = (o_index-instruction["value"]//90)%4
	elif instruction["opcode"] == "F":
		position = position+orientations[o_index]*instruction["value"]
print(np.sum(np.absolute(position)))

# Part 2
ship = np.array([0,0])
wp = np.array([10,1])
for instruction in instructions:
	if instruction["opcode"] in ["N","S","E","W"]:
		wp = wp+translations[instruction["opcode"]]*instruction["value"]
	elif instruction["opcode"] == "L":
		for _ in range(instruction["value"]//90):
			wp = np.array([-wp[1],wp[0]])
	elif instruction["opcode"] == "R":
		for _ in range(instruction["value"]//90):
			wp = np.array([wp[1],-wp[0]])
	elif instruction["opcode"] == "F":
		ship = ship+wp*instruction["value"]
print(np.sum(np.absolute(ship)))
