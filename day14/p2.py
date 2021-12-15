def parce(inputfile="input.txt"):
	with open(inputfile, 'r') as file:
		arr = file.readlines()
		polymer_template = arr.pop(0).replace("\n", "")
		arr.pop(0) # get rid of new line
		table = dict()
		for item in arr:
			item = item.split(" -> ")
			table[item[0]] = item[1].replace("\n", "")

	return (polymer_template, table)

class folder:

	def __init__(self, start, table):
		self.table = table
		self.curr = dict()

		for i in range(len(start)-1):
			key = start[i]+start[i+1]
			if not key in self.curr:
				self.curr[key] = 0
			self.curr[key] += 1


	def do_cycle(self):
		new_dict = dict()
	

		for key in self.table:
			if not key in new_dict:
				new_dict[key] = 0
			if not key in self.curr:
				self.curr[key] = 0


			amount = self.curr[key] 
			key1 = key[0] + self.table[key]
			key2 = self.table[key] + key[1]

			if not key1 in new_dict:
				new_dict[key1] = 0
			if not key2 in new_dict:
				new_dict[key2] = 0

			new_dict[key1] += amount
			new_dict[key2] += amount

		self.curr = new_dict


	def get_common_diff(self):
		count = dict()
		for key in self.curr:
			if not key[0] in count:
				count[key[0]] = 0
			if not key[1] in count:
				count[key[1]] = 0

			count[key[0]] += self.curr[key]
			count[key[1]] += self.curr[key]

		count["V"] += 2
		all_vals = set(count.values())

		return (max(all_vals) - min(all_vals))//2

	def get_empty(self):
		for key in self.table:
			if(self.curr[key] == 0):
				print(f'{key}: 0')

start, table = parce()
f = folder(start, table)

for i in range(40):
	print(f"Cycle: {i} {sum(f.curr.values())}")
	f.do_cycle()
#f.get_empty()
print(f.get_common_diff())
