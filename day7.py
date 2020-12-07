s = []
with open("tmp.txt","r") as i:
	s = i.read()
s = s.strip()

bags = []
for rule in s.split("\n"):
	parsed_bag = {}
	parsed_bag["color"] = rule.split(" bags contain ")[0]
	parsed_bag["children"]=[]
	for child in rule.split(" bags contain ")[1].split(", "):
		if child[0:2]=="no":
			break	
		parsed_bag["children"].append({
		"amount" : int(child.split(" ")[0]),
		"color" : " ".join(child.split(" ")[1:-1])
		})
	bags.append(parsed_bag)

# Part 1
containers = []
nb_containers = 0
containers = [bag for bag in bags if "shiny gold" in [child["color"] for child in bag["children"]]]
while nb_containers<len(containers):
	nb_containers=len(containers)
	containers += [bag for bag in bags if any([container["color"] in [child["color"] for child in bag["children"]] for container in containers]) and bag not in containers]
print("Number of possible bags")
print(len(containers))

# Part 2
def get_nb_inner_bags(color):
	nb_inner_bags=0
	bag = [_ for _ in bags if _["color"]==color][0]
	for child in bag["children"]:
		nb_inner_bags = nb_inner_bags+child["amount"]+child["amount"]*get_nb_inner_bags(child["color"])
	return nb_inner_bags
print("Number of inner bags necessary")
print(get_nb_inner_bags("shiny gold"))