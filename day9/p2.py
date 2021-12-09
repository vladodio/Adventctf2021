#from time import sleep

class Map():

	def __init__(self, arr):
		self.map = arr
		self.x_width = len(arr[0])
		self.y_width = len(arr)

	def check_chord(self, x, y):
		#        u     d     l     r
		check = [True, True, True, True]
		
		if(y == 0):
			check[1] = False
		if(y == self.y_width-1):
			check[0] = False

		if(x == 0):
			check[2] = False
		if(x == self.x_width-1):
			check[3] = False

		bottom = True
		# up
		if(check[0]):
			if(not self.map[x][y] < self.map[x][y+1]):
				bottom = False

		# down
		if(check[1]):
			if(not self.map[x][y] < self.map[x][y-1]):
				bottom = False

		# left
		if(check[2]):
			if(not self.map[x][y] < self.map[x-1][y]):
				bottom = False

		# right
		if(check[3]):
			if(not self.map[x][y] < self.map[x+1][y]):
				bottom = False

		return(bottom)

	def find_all_basins(self):
		self.basins = list()
		for i in range(self.x_width):
			for j in range(self.y_width):
				if(a.check_chord(i, j)):
					self.basins.append((i,j))
		return self.basins

	def find_basin_size(self, x, y):
		queue = list()
		visited = list()

		queue.extend(self.return_non_nine_adj(x,y))
		size = 0
		print(queue)
		while(len(queue) != 0):
			#print(queue)
			#print(visited)
			#sleep(1)
			coords = queue.pop(0)

			if(coords in visited):
				continue

			queue.extend(self.return_non_nine_adj(coords[0],coords[1]))
			size+=1
			visited.append(coords)

			new_queue = list()
			for i in range(len(queue)):
				not_found = True
				for j in range(len(visited)):
					if(queue[i] == visited[j]):
						not_found = False
						break

				if(not_found):
					new_queue.append(queue[i])
			queue = new_queue

		return size


	def return_non_nine_adj(self, x, y):
		#        u     d     l     r
		check = [True, True, True, True]
		outset = set()

		if(y == 0):
			check[1] = False
		if(y == self.y_width-1):
			check[0] = False

		if(x == 0):
			check[2] = False
		if(x == self.x_width-1):
			check[3] = False

		#	print(x,y)
		# up
		if(check[0]):
			if(self.map[x][y+1] != 9):
				outset.add((x,y+1))

		# down
		if(check[1]):
			if(self.map[x][y-1] != 9):
				outset.add((x,y-1))

		# left
		if(check[2]):
			if(self.map[x-1][y] != 9):
				outset.add((x-1,y))

		# right
		if(check[3]):
			if(self.map[x+1][y] != 9):
				outset.add((x+1,y))
		#print(outset)
		return outset


	def __str__(self):
		pass




def parce(inputfile="input.txt"):
	with open(inputfile, 'r') as file:
		arr = file.readlines()
		outarr = list()
		for i in range(len(arr)):
			outarr.append(list())
			arr[i] = arr[i].replace("\n", "")
			for item in arr[i]:
				outarr[i].append(int(item))
	return outarr

a = Map(parce())
basins = a.find_all_basins()
x,y = basins[0]

basin_sizes = list()
for basin in basins:
	basin_sizes.append(a.find_basin_size(basin[0],basin[1]))
basin_sizes.sort()
print(basin_sizes)