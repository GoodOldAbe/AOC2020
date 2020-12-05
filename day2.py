s = []
with open("tmp.txt","r") as i:
	s = i.readlines()
records = []
for line in s:
	line = line.strip()
	records.append({"min":int(line.split("-")[0]),
	"max":int(line.split(" ")[0].split("-")[1]),
	"letter":line.split(" ")[1][0],
	"password":line.split(" ")[-1]})
print(records)

nb_valid = 0
for record in records:
	letters = [_ for _ in record["password"]]
	if record["min"]<=letters.count(record["letter"])<=record["max"]:
		nb_valid+=1
print("Number of valid passwords in first half")
print(nb_valid)

nb_valid = 0
for record in records:
	if (record["password"][record["min"]-1]==record["letter"]) ^ (record["password"][record["max"]-1]==record["letter"]):
		nb_valid+=1
print("Number of valid passwords in second half")
print(nb_valid)