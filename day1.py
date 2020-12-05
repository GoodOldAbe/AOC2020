s = []
with open("tmp.txt","r") as i:
	s = i.readlines()
numbers = [int(_.strip()) for _ in s if _.strip()]
numbers.sort()

for x in numbers:
	for y in numbers:
		for z in numbers:
			if x+y+z==2020:
				print("{} {} {}".format(x,y,z))
				print(x*y*z)
				break
		if x+y+z==2020:
			break
	if x+y+z==2020:
		break