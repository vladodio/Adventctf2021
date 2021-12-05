
class board():

	def __init__(self):
		#self.lines = set()
		self.board = [[0] * 1000 for i in range(1000)]

	def add_line(self, start, end):
		#self.lines.add((int(start), int(end), list()))
		self.process_line(int(start[0]), int(start[1]), int(end[0]), int(end[1]))

	def process_line(self, startX, startY, endX, endY):
		# verti line
		if(startX == endX):
			for i in range(min(startY, endY), max(startY, endY)+1):
				self.board[startX][i] += 1

		# hori line
		elif(startY == endY):
			for i in range(min(startX, endX), max(startX, endX)+1):
				self.board[i][startY] += 1
		#diagonal
		else:
			# going right
			if(startX < endX):
				diag_diff_X = 1
			
			# going left
			else:
				diag_diff_X = -1

			# going up
			if(startY < endY):
				diag_diff_Y = 1
			# going down
			else:
				diag_diff_Y = -1

			length = max(startX, endX) - min(startX, endX)
			print(length)
			for i in range(length+1):
				#print(i, startX + (i*diag_diff_X), startY + (i+diag_diff_Y))
				self.board[startX + (i*diag_diff_X)][startY + (i*diag_diff_Y)] += 1


	def count(self):
		total = 0
		for row in self.board:
			for item in row:
				if(item >= 2):
					total += 1
		return total



	def __str__(self):
		outstr = ""
		for line in self.board:
			outstr+= str(line[:50]).replace(",", "").replace("0", ".") + '\n'
		return outstr


def parce(inputfile="input.txt"):
	with open(inputfile, 'r') as file:
		outarr = list()
		for line in file:
			outarr.append(line.replace("\n", "").split(" -> "))
	return outarr

arr = parce()
#print(arr)
a = board()

for item in arr:
	#a.add_line(item[0], item[1])
	start = item[0].split(",")
	end = item[1].split(",")
	print(f'{start}, {end}')
	a.add_line(start, end)

print(a.count())
#print(a)