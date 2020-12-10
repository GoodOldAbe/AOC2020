import itertools
s = []
with open("tmp.txt","r") as i:
	s = i.read()
s = s.strip()

# Part 1
adapters = sorted([int(_) for _ in s.split("\n")])
jolt=0
delta_1 = 0
delta_3 = 1
for adapter in adapters:
	if adapter-jolt>3:
		print("Problem")
		break
	elif adapter-jolt==1:
		delta_1+=1
	elif adapter-jolt==3:
		delta_3+=1
	jolt = adapter
print(delta_1*delta_3)

# Part 2
compute_dyn = []
for index in range(len(adapters)):
	if index==0:
		compute_dyn.append(1)
	else:
		count = 0
		if index>=1 and adapters[index]-adapters[index-1]<=3:
			count+=compute_dyn[index-1]
		if index>=2 and adapters[index]-adapters[index-2]<=3:
			count+=compute_dyn[index-2]
		if index>=3 and adapters[index]-adapters[index-3]<=3:
			count+=compute_dyn[index-3]
		if adapters[index]<=3:
			count+=1
		compute_dyn.append(count)
print(compute_dyn[-1])