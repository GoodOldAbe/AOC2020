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
def compute(local_set):
	if len(local_set)==2:
		print(local_set)
		print(1)
		return 1
	count = 0
	combinations = [[local_set[0],local_set[-1]]]
	for n in range(1,len(local_set)-1):
		combinations += [[local_set[0]]+list(_)+[local_set[-1]] for _ in itertools.combinations(local_set[1:-1],n)]
	for combination in combinations:
		if all([combination[i]-combination[i-1]<=3 for i in range(1,len(combination))]):
			count+=1
	print([combination for combination in combinations if all([combination[i]-combination[i-1]<=3 for i in range(1,len(combination))])])
	print(count)
	return count

nb_arrangments = 1
local_set = [0]
for index in range(len(adapters)-1):
	local_set.append(adapters[index])
	if adapters[index+1]-adapters[index-1]>3:
		nb_local_arrangments = compute(local_set)
		nb_arrangments = nb_arrangments*nb_local_arrangments
		local_set = [adapters[index]]
	elif index==len(adapters)-2:
		local_set.append(adapters[-1])
		nb_local_arrangments = compute(local_set)
		nb_arrangments = nb_arrangments*nb_local_arrangments
print(nb_arrangments)
