import math

s = []
with open("tmp.txt","r") as i:
	s = i.read()
s = s.strip()

instructions = []
for line in s.split("\n"):
	command, value = line.split(" = ")
	if command == "mask":
		instructions.append({"command":command, "value":value})
	else:
		instructions.append({"command":int(command[4:-1]), "value":int(value)})

# Part 1
memory = {}
mask = 36*"0"
for instruction in instructions:
	if instruction["command"]=="mask":
		mask = instruction["value"]
	else:
		i = instruction["value"]
		for index in range(len(mask)):
			if mask[index]=="0":
				i = i & ((2**36-1)-2**(36-index-1))
			elif mask[index]=="1":
				i = i | 2**(36-index-1)
		memory[instruction["command"]]=i
out = 0
for key in memory.keys():
	out+=memory[key]
print(out)

# Part 2
memory = {}
mask = 36*"0"
for instruction in instructions:
	if instruction["command"]=="mask":
		mask = instruction["value"]
	else:
		adresses = [instruction["command"]]
		for index in range(len(mask)):
			nb_adresses = len(adresses)
			for _ in range(nb_adresses):
				if mask[index]=="1":
					adresses[_] = adresses[_] | 2**(36-index-1)
				elif mask[index]=="X":
					adresses[_] = adresses[_] & ((2**36-1)-2**(36-index-1))
					adresses.append(adresses[_] | 2**(36-index-1))
		for adress in adresses:
			memory[adress]=instruction["value"]
out = 0
for key in memory.keys():
	out+=memory[key]
print(out)