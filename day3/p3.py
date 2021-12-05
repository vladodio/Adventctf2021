#!/usr/bin/env python3


class bst:


	def __init__(self, leng=12):
		self.leng = leng
		self.digits = [0] * leng

		self.tree = [0] * 4096

	def insert(self, digit):
		self.tree[int(digit, 2)] = True


	def sum(self, start, end, mid):		
		zero_counter = 0;
		one_counter = 0
		
		for i in range(start, mid):
			if(self.tree[i]):
				zero_counter += 1

		for i in range(mid, end):
			if(self.tree[i]):
				one_counter += 1

		return(zero_counter < one_counter)

	def find_co2(self):
		start = 0
		end = len(self.tree)

		for i in range(11):
			mid = int((end - start)/2)+start
			if(self.sum(start, end, mid)):
				start = mid
			else:
				end = mid

		# go to the right for final case

		print(f'{start} : {end}')
		print(self.tree[start])
		return 1





	def __str__(self):
		return str(self.tree)


def openFile(filename="input.txt"):
	with open("input.txt", 'r') as file:
		return(file.readlines())


def main():
	b = bst()
	file = openFile()

	for line in file:
		b.insert(line)

	b.find_co2()
	#b.find_o2()



if __name__ == '__main__':
	main()