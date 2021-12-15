error_vals = {
	')' : 3,
	']' : 57,
	'}' : 1197,
	'>' : 25137
}

openers = {'(', '[', '{', '<'}
closers = {')', ']', '}', '>'}

matching = {
	')' : '(',
	']' : '[',
	'}' : '{',
	'>' : '<'
}


def parce(inputfile="input.txt"):
	with open(inputfile, 'r') as file:
		arr = file.readlines()
		for i in range(len(arr)):
			arr[i] = arr[i].replace("\n", "")
		return arr

def process_line(line):
	stack = list()
	error_val = 0

	for char in line:
		if(char in openers):
			stack.append(char)

		elif(char in closers):
			if(matching[char] != stack.pop()):
				print(char)
				return error_vals[char]


	if(len(stack) != 0):
		return 0


arr = parce()
#print(arr)
sumall = 0
for line in arr:
	sumall += process_line(line)
print(sumall)