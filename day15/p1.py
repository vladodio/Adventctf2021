from queue import PriorityQueue

def parce(inputfile="input.txt"):
	with open(inputfile, 'r') as file:
		arr = file.readlines()
		outarr = list()
		for line in arr:
			new_line = list()
			for char in line.replace("\n", "").strip():
				new_line.append(int(char))
		outarr.append(new_line)
	return outarr


class map():

	def __init__(self, arr):
		self.map = arr
		self.start = (0,0)
		self.end = (len(arr)-1, len(arr[0])-1)

	def shortest_path_sum(self):
		# queue
		queue = PriorityQueue()
		queue.put((0, self.start))
		# visited set
		visited = set()

		while(not queue.empty()):
			curr_weight, curr_coords = queue.get()
			
			#print(curr_coords)
			if(curr_coords[0] == self.end[0] and curr_coords[1] == self.end[1]):
				return curr_weight

			if(curr_coords in visited):
				continue

			visited.add(curr_coords)

			print(f'Visited : {len(list(visited))}')
			
			conn = self.ret_connected(curr_coords)
			for connection in conn:
				if(not connection in visited):
					queue.put((curr_weight + self.map[connection[0]][connection[1]], (connection[0],connection[1]) ))





	def ret_connected(self, xy):
		x, y = xy
		connected = list()
		for diff in [(1,0), (0,1), (-1, 0), (0, -1)]:
			try:
				if((diff[0] + x < 0) or (diff[1] + y) < 0 ):
					continue
				self.map[diff[0] + x][diff[1] + y]
				connected.append( ( (x+diff[0]), (y+diff[1]) ) )
			except:
				pass
		return connected

def gen_map(map):
	big_map = [ [0] * 5 for i in range(5)]


arr = parce()
m = map(arr)
#print(m.map)
print(m.shortest_path_sum())