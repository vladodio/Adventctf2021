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


def do_cycle(start, table):
	outstr = ""
	counter = 0
	for i in range(len(start)-1):
		outstr += start[i]
		outstr += table[start[i:i+2]]
	outstr += start[-1]
	return outstr

def get_common_diff(string):
	table = dict()
	char_set = set(string)
	for char in char_set:
		table[char] = 0

	for char in string:
		table[char] += 1

	mc_letter = ""
	mc_amount = -1000

	lc_letter = ""
	lc_amount = 10000000000 

	for char in char_set:
		if(table[char] > mc_amount):
			mc_letter = char
			mc_amount = table[char]
		if(table[char] < lc_amount):
			lc_amount = table[char]
			lc_letter = char
	print(mc_amount, lc_amount)
	return mc_amount- lc_amount

start, table = parce()

for i in range(10):
	print(f"Cycle: {i} {len(start)}")
	start = do_cycle(start, table)

for i in ["BB","FS","OH","FV","HO","PC","ON","VB","KV","FP","KS","PH","HS","KP","FO","NP","VK"]:
	print(i in start)

print(get_common_diff(start))