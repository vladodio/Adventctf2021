

class Fish_Array():

	def __init__(self):
		self.fish_arr = [0] * 9


	def add(self, day, amount=1):
		self.fish_arr[day] += amount


	def run_cycle(self):
		new_array = [0]*9
		# make new children
		new_array[-1] = self.fish_arr[0]
		# reset fish that just made children
		new_array[6] = self.fish_arr[0]

		# copy over everything else
		for i in range(len(self.fish_arr)-1):
			new_array[i] += self.fish_arr[i+1]
		self.fish_arr = new_array

	def __str__(self):
		return(str(self.fish_arr))

	def sum(self):
		sum = 0
		for item in self.fish_arr:
			sum += item
		return sum


def parce(inputfile="input.txt"):
	with open(inputfile, 'r') as file:
		arr = file.readlines()[0].split(",")
		fish_arr = Fish_Array()
		for item in arr:
			fish_arr.add(int(item))

	return fish_arr

'''
for item in parce():
	print(item)
'''

fish_arr = parce()
cycles = 256

for i in range(cycles):
	fish_arr.run_cycle()

print(fish_arr.sum())
