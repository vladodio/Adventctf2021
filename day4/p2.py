import re
# copied out of txt for ease
winning_answers = [37,60,87,13,34,72,45,49,61,27,97,88,50,30,76,40,63,9,38,67,82,6,59,90,99,54,11,66,98,23,64,14,18,4,10,89,46,32,19,5,1,53,25,96,2,12,86,58,41,68,95,8,7,3,85,70,35,55,77,44,36,51,15,52,56,57,91,16,71,92,84,17,33,29,47,75,80,39,83,74,73,65,78,69,21,42,31,93,22,62,24,48,81,0,26,43,20,28,94,79]


class Board():


	def __init__(self, arr):
		self.board = [0] * 25
		self.bits = [False] * 25

		pos = 0
		for item in arr:
			if(item == ''):
				continue
			self.board[pos] = int(item)
			pos += 1 

	def check_digit(self, digit):
		if(not digit in self.board):
			return -1

		location = [i for i in range(len(self.board)) if self.board[i] == digit]
		self.bits[location[0]] = True
		return(self.check_for_win())
		
	def check_for_win(self):
		# check row
		for i in [0, 5, 10, 15, 20]:
			if(self.bits[i] and self.bits[i+1] and self.bits[i+2] and self.bits[i+3] and self.bits[i+4]):
				return 1

		# check col
		indexs = [0, 5, 10, 15, 20]
		for i in range(5):
			if(self.bits[indexs[0]+i] and self.bits[indexs[1]+i] and self.bits[indexs[2]+i] and self.bits[indexs[3]+i] and self.bits[indexs[4]+i]):
				return 1
		
		return 0		


	def __str__(self):
		sum = 0
		for i in range(len(self.board)):
			if(not self.bits[i]):	
				sum += self.board[i]
		return str(sum)


def parce(inputfile="input.txt"):
	boards = list()
	outarr = list()
	with open(inputfile, 'r+') as file:
		f = file.read()
		outarr = f.replace("\n", "X").split("XX")
		for i in range(len(outarr)):
			outarr[i] = outarr[i].replace("X", " ").replace("  ", " ").split(" ")
		#print(outarr)
	return outarr



arr = parce()
boards = list()
for item in arr:
	boards.append(Board(item))



for digit in winning_answers:
	if(len(boards) == 1):
		print(boards[0].check_digit(digit))
		print(boards[0])
		print(digit)
		print(digit*int(str(boards[0])))

	outarr = list()
	for b in boards:
		if(b.check_digit(digit) != 1):
			outarr.append(b)

	boards = outarr

		
