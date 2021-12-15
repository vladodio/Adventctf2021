def parce(inputfile="input.txt"):
	outlist = list()
	with open(inputfile, 'r') as file:
		for line in file.readlines():
			outlist.append(line.strip().split("-"))
	return outlist

class Node:

	def __init__(self, nodeName):
		self.name = nodeName
		self.connections = list()

		if(nodeName == nodeName.upper()):
			self._isSmall = False
		else:
			self._isSmall = True

	def isSmall(self):
		return self._isSmall

	def getName(self):
		return self.name

	def add_connection(self, node):
		self.connections.append(node)

	def getConnections(self):
		return self.connections

	def isEnd(self):
		return self.getName() == "end"

	def __hash__(self):
		return hash(self.name)

	def __str__(self):
		outstr = self.getName() + ": "
		for connection in self.connections:
			outstr += connection.getName() + " "
		outstr+= "\n"
		return outstr


class Graph():

	def __init__(self):
		self.node_name_set = set()
		self.node_set = set()

	def get_node(self, name):
		for item in self.node_set:
			if(item.getName() == name):
				return item
		print("not found")

	def add(self, nodeA, nodeB):
		if not nodeA in self.node_name_set:
			nodeA_obj = Node(nodeA)
			self.node_name_set.add(nodeA)
			self.node_set.add(nodeA_obj)
		else:
			nodeA_obj = self.get_node(nodeA)
	
		if not nodeB in self.node_name_set:
			nodeB_obj = Node(nodeB)
			self.node_name_set.add(nodeB)
			self.node_set.add(nodeB_obj)
		else:
			nodeB_obj = self.get_node(nodeB)
		
		nodeB_obj.add_connection(nodeA_obj)
		nodeA_obj.add_connection(nodeB_obj)

		if(nodeA_obj.getName() == "start"):
			self.start = nodeA_obj
		if(nodeB_obj.getName() == "start"):
			self.start = nodeB_obj

	def getStart(self):
		return self.start

	def __str__(self):
		outstr = "Graph\n"
		for node in self.node_set:
			outstr += str(node)
		return outstr


counter = 0
def recursive_path_find(currNode, visited):
	global counter
	if(currNode.isEnd()):
		counter += 1
		return

	toVisit = list()
	for conn in currNode.getConnections():
		if(not conn.isSmall()) or (not conn.getName() in visited):
			toVisit.append(conn)

	for node in toVisit:
		recursive_path_find(node, visited + " " + currNode.getName())
	return


arr = parce()
g = Graph()
for pair in arr:
	g.add(pair[0], pair[1])

print(g)
recursive_path_find(g.getStart(), "")
print(counter)


