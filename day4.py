import re
s = []
with open("tmp.txt","r") as i:
	s = i.read()

passports = s.split("\n\n")
passports = [sum([line.split(" ") for line in passport.split("\n")],[]) for passport in passports]

# Part 1
passports_fields = [[entry.split(":")[0] for entry in passport] for passport in passports]
nb_valid_passports = 0
for passport in passports_fields:
	if {"byr","iyr","eyr","hgt","hcl","ecl","pid"}.issubset(set(passport)):
		nb_valid_passports+=1
print(nb_valid_passports)

# Part 2
nb_valid_passports = 0
passports = [{k:v for k,v in [tuple(entry.split(":")) for entry in passport]} for passport in passports]
for passport in passports:
	if {"byr","iyr","eyr","hgt","hcl","ecl","pid"}.issubset(set(passport.keys())) and \
		1920<=int(passport["byr"])<=2002 and \
		2010<=int(passport["iyr"])<=2020 and \
		2020<=int(passport["eyr"])<=2030 and \
		((passport["hgt"][-2:]=="cm" and 150<=int(passport["hgt"][:-2])<=193) or (passport["hgt"][-2:]=="in" and 59<=int(passport["hgt"][:-2])<=76)) and \
		re.search("^#[0-9a-f]{6,6}$",passport["hcl"]) and \
		passport["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"] and \
		re.search("^[0-9]{9,9}$",passport["pid"]):
		nb_valid_passports+=1
print(nb_valid_passports)
