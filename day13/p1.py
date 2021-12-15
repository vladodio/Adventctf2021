class Paper:

	def __init__(self, arr, x, y):
		self.graph = [[0] * y for i in range(x)]
		self._parce_coords(arr)
		self.x = x
		self.y = y

	def _parce_coords(self, arr):
		for coords in arr:
			self.graph[int(coords[0])][int(coords[1])] = 1

	def do_fold(self, command):
		args = command.split(" ")[2].split("=")
		args[1] = int(args[1])

		if(args[0] == "x"):
			for i in range(args[1]):
				for j in range(self.y):
					curr_x = (args[1] -i) + args[1]
					self.graph[i][j] += self.graph[curr_x][j]
					self.graph[curr_x][j] = 0


		elif(args[0] == "y"):
			for i in range(self.x):
				for j in range(args[1]):
					curr_y = (args[1] -j) + args[1]
					self.graph[i][j] += self.graph[i][curr_y]
					self.graph[i][curr_y] = 0
		else:
			print("error?", args)

	def count_dots(self):
		count = 0
		for line in self.graph:
			for item in line:
				if(item != 0):
					count += 1
		return count


	def __str__(self):
		outstr = ""
		for i in range(self.x):
			for j in range(self.y):
				outstr += str(self.graph[i][j]) + " "
			outstr += "\n"
		return outstr	

	def printer(self, x, y):
		outstr = ""
		for i in range(x):
			for j in range(y, -2, -1):
				if(self.graph[i][j] != 0):
					outstr += "# "
				else:
					outstr += ". "
			outstr += "\n"
		return outstr	



def parce(inputfile="input.txt"):
	with open(inputfile, 'r') as file:
		arr = file.readlines()
		coords = list()
		folds = list()
		for i in range(len(arr)):
			arr[i] = arr[i].replace("\n", "")
			if(arr[i][:4] == "fold"):
				folds.append(arr[i])
			elif(arr[i] == ""):
				continue
			else:
				coords.append(arr[i].replace("(", "").replace(")", "").split(","))
	return (coords, folds)



coords, folds  =  parce()
p = Paper(coords, 1500, 1500)


for fold in folds:
	p.do_fold(fold)
	print(fold)
'''
p.do_fold(folds[0])
print(p.count_dots())
'''
print(p.printer(40, 6))