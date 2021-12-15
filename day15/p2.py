from queue import PriorityQueue

def inc_and_wrap(i, j):
	return ((i+j-1) % 9) + 1

# return first row
def parce(inputfile="input.txt"):
	with open(inputfile, 'r') as file:
		arr = file.readlines()
		outarr = list()
		for line in arr:
			lines = [list(), list(), list(), list(), list()]
			for char in line.replace("\n", "").strip():
				val = int(char)
				# build the first row
				for i in range(5):
					lines[i].append(inc_and_wrap(val, i))
			
			print(len(lines[0]))
			for i in range(1,5):
				lines[0].extend(lines[i])
			outarr.append(lines[0])
	return outarr


class Map():

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

	def __str__(self):
		outstr = ""
		for line in self.map:
			for char in line:
				outstr += str(char)
			outstr += "\n"
		return outstr


def gen_map(given_map):
	curr_row = given_map

	for i in range(1, 5):
		print(i)
		next_row = list()
		for row in curr_row:
			processing_row = list()	
			for char in row:
				print(inc_and_wrap(char, i), end='')
				processing_row.append(inc_and_wrap(char, 1))
			next_row.append(processing_row)
		print("")
		given_map.extend(next_row)
		curr_row = next_row
	return given_map


arr = parce()
#print(gen_map(arr))
m = Map(gen_map(arr))
#print(m)
print(m.shortest_path_sum())