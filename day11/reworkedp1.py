# not done, while writing figured out problem with part 1

direction_vectors = {(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)}
class Board:

	def __init__(self, arr):
		pass

	def __init__(self, arr):
		self.map = arr
		
		self.y_height = len(arr)
		self.x_width = len(arr[0])
	
	def inc_squids(self):
		for i in range(self.y_height):
			for j in range(self.x_width):
				self.map[i][j] += 1

	def process_squids(self):
		element_updated = True

		while(element_updated):
			element_updated = False
			for i in range(self.y_height):
				for j in range(self.x_width):
					if(self.map[i][j] > 9):
						process_squid(i,j)


	def process_squid(self, x, y):
		for vector in direction_vectors:
			try:
				if((vector[0] + x < 0) or (vector[1] + y) < 0 ):
					continue
				self.map[]

	def run_cycle(self):
		self.inc_squids()
		self.process_squids()
		self.clear_squids()