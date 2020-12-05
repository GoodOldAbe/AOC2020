s = []
with open("tmp.txt","r") as i:
	s = i.readlines()

matrix = [[_ for _ in row.strip()] for row in s]
nb_rows = len(matrix)
nb_columns = len(matrix[0])

# Part 1
position = [0,0]
nb_trees = 0
while position[0]<nb_rows-1:
	position[0]+=1
	position[1]=(position[1]+3)%nb_columns
	if matrix[position[0]][position[1]]=="#":
		nb_trees+=1
print(nb_trees)

# Part 2
def compute_nb_tree(matrix,deltax,deltay):
	nb_rows = len(matrix)
	nb_columns = len(matrix[0])
	position = [0,0]
	nb_trees = 0
	while position[0]<nb_rows-deltax:
		position[0]+=deltax
		position[1]=(position[1]+deltay)%nb_columns
		if matrix[position[0]][position[1]]=="#":
			nb_trees+=1
	return nb_trees

print(compute_nb_tree(matrix,1,1)*compute_nb_tree(matrix,1,3)*compute_nb_tree(matrix,1,5)*compute_nb_tree(matrix,1,7)*compute_nb_tree(matrix,2,1))