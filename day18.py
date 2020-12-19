import math
import re

s = []
with open("tmp.txt","r") as i:
	s = i.read()
s = s.strip()

s = s.replace(" ","")

def compute(calcul):
	calcul = re.split('([*+])',calcul)
	output = int(calcul[0])
	calcul = calcul[1:]
	while True:
		if calcul[0]=="*":
			output*=int(calcul[1])
		else:
			output+=int(calcul[1])
		if len(calcul)==2:
			break
		else:
			calcul = calcul[2:]
	return output

def adv_compute(calcul):
	return math.prod([sum([int(_) for _ in segment.split("+")]) for segment in calcul.split("*")])


# Part 1
output = 0
for calcul in s.split("\n"):
	while "(" in calcul:
		start = calcul.index("(")+1
		end = start
		while end+1<len(calcul):
			if calcul[end]=="(":
				start = end+1
				end = end+1
			else:
				end = end+1
			if calcul[end]==")":
				break
		if start == 1:
			calcul = str(compute(calcul[start:end]))+calcul[end+1:]
		elif end+1 == len(calcul):
			calcul = calcul[:start-1]+str(compute(calcul[start:end]))
		else:
			calcul = calcul[:start-1]+str(compute(calcul[start:end]))+calcul[end+1:]
	output+=compute(calcul)
print(output)

# Part 2
output = 0
for calcul in s.split("\n"):
	while "(" in calcul:
		start = calcul.index("(")+1
		end = start
		while end+1<len(calcul):
			if calcul[end]=="(":
				start = end+1
				end = end+1
			else:
				end = end+1
			if calcul[end]==")":
				break
		if start == 1:
			calcul = str(adv_compute(calcul[start:end]))+calcul[end+1:]
		elif end+1 == len(calcul):
			calcul = calcul[:start-1]+str(adv_compute(calcul[start:end]))
		else:
			calcul = calcul[:start-1]+str(adv_compute(calcul[start:end]))+calcul[end+1:]
	output+=adv_compute(calcul)
print(output)