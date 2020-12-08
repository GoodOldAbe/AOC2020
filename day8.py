import copy

s = []
with open("tmp.txt","r") as i:
	s = i.read()
s = s.strip()
instructions = [{"operand":_.split(" ")[0],"value":int(_.split(" ")[1])} for _ in s.split("\n")]

# Part 1
position = 0
executed = []
acc = 0
while position not in executed:
	executed.append(position)
	if instructions[position]["operand"]=="acc":
		acc += instructions[position]["value"]
	if instructions[position]["operand"] != "jmp":
		position += 1
	else:
		position += instructions[position]["value"]
print(acc)

# Part 2
def run_program(instructions):
	position = 0
	executed = []
	acc = 0
	while position not in executed and position<len(instructions):
		executed.append(position)
		if instructions[position]["operand"] == "acc":
			acc += instructions[position]["value"]
		if instructions[position]["operand"] != "jmp":
			position += 1
		else:
			position += instructions[position]["value"]
	return [position==len(instructions), acc]

for index in range(len(instructions)):
	test_instructions = copy.deepcopy(instructions)
	if test_instructions[index]["operand"] == "jmp":
		test_instructions[index]["operand"] = "nop"
	elif test_instructions[index]["value"] == "nop":
		test_instructions[index]["operand"] = "jmp"
	else:
		continue
	[success,acc] = run_program(test_instructions)
	if success:
		print("Success !")
		print(acc)
