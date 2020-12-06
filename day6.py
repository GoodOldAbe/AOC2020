from collections import Counter

s = []
with open("tmp.txt","r") as i:
	s = i.read()
s = s.strip()
groups = s.split("\n\n")

# Part 1
groups = ["".join(group.split("\n")) for group in groups]
groups = [Counter([_ for _ in group]) for group in groups]
print(sum([len(group.keys()) for group in groups]))

# Part 2
groups = s.split("\n\n")
groups = [[set([_ for _ in answers]) for answers in group.split("\n")] for group in groups]
print(sum([len(group[0].intersection(*group)) for group in groups]))
