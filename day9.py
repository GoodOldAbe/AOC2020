s = []
with open("tmp.txt","r") as i:
	s = i.read()
s = s.strip()
numbers = [int(_) for _ in s.split("\n")]

# Part 1
for index in range(26,len(numbers)):
	target = numbers[index]
	candidates = numbers[index-25:index]
	lh = [_ for _ in candidates if _<=target//2]
	uh = [_ for _ in candidates if _>target//2]
	found = False
	for l in lh:
		for u in uh:
			if l+u==target and not found:
				found=True
	if not found:
		print(target)
		break

# Part 2
found = False
for size in range(2,len(numbers)):
	ub = [_>target//size for _ in numbers]
	for index in range(len(numbers)-size+1):
		if any(ub[index:index+size]) and any([not _ for _ in ub[index:index+size]]):
			if sum(numbers[index:index+size])==target:
				found=True
				print(numbers[index:index+size])
				print(min(numbers[index:index+size])+max(numbers[index:index+size]))
				break
	if found:
		break