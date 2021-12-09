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

arr = parce()

a = Map(arr)
sum_of_risk = 0
for i in range(a.x_width):
	for j in range(a.y_width):
		if(a.check_chord(i, j)):
			print(f'({i},{j})')
			sum_of_risk += a.map[i][j] + 1
print(sum_of_risk)