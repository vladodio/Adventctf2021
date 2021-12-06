
class Fish():

	def __init__(self, day=8):
		self.day = day

	def run_cycle(self):
		if(self.day == 0):
			self.day = 6
			return True
		else:
			self.day -= 1
			return False

	def __str__(self):
		return str(self.day)



def parce(inputfile="input.txt"):
	with open(inputfile, 'r') as file:
		arr = file.readlines()[0].split(",")
		outarr = list()
		for item in arr:
			outarr.append(Fish(int(item)))

	return outarr

'''
for item in parce():
	print(item)
'''

fish_arr = parce()
cycles = 80

for i in range(cycles):
	updated_arr = list(fish_arr)
	for fish in fish_arr:
		if(fish.run_cycle()):
			updated_arr.append(Fish())
	fish_arr = updated_arr
print(len(fish_arr))
