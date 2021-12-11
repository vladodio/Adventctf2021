class Board:

	def __init__(self, arr):
		self.map = arr
		
		self.y_width = len(arr)
		self.x_width = len(arr[0])
		
		self.total_fired = 0
		self.total_zeroed = 0
		self.fired = [[False] * self.x_width for i in range(self.y_width)]
		


	def clear_fired(self):
		for i in range(len(self.fired)):
			for j in range(len(self.fired[i])):
				self.fired[i][j] = False

	def count_fired(self):
		count = 0
		for i in range(len(self.fired)):
			for j in range(len(self.fired[i])):
				if(self.fired[i][j]):
					count += 1
		self.total_fired += count
		return count


	def process_space(self, x, y):
		if(self.map[x][y] > 9 and self.fired[x][y] == False):
			for diff in [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]:
				try:
					if((diff[0] + x < 0) or (diff[1] + y) < 0 ):
						continue
					self.map[x+diff[0]][y+diff[1]] += 1
				except:
					pass
			self.fired[x][y] = True
			return True
		else:
			return False


	def inc_all_squid(self):
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				self.map[i][j] += 1

	def set_to_zero(self):
		count = 0
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				if(self.map[i][j] > 9):
					self.map[i][j] = 0
					count += 1


	def run_cycle(self):
		self.clear_fired()
		self.inc_all_squid()

		updated = True
		while(updated):
			updated = False
			for i in range(len(self.map)):
					for j in range(len(self.map[i])):

						if(self.fired[i][j] == False):
							if(self.process_space(i,j)):
								updated = True


		self.set_to_zero()
		return self.count_fired()


	def __str__(self):
		outstr = str()
		for line in self.map:
			for char in line:
				outstr += str(char) + " "
			outstr += "\n"
		return outstr



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

b = Board(arr)

for i in range(100):
	b.run_cycle()
	print(b.total_fired)
	print(b)
	print("--------------------------")