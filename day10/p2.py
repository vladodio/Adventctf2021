openers = {'(', '[', '{', '<'}
closers = {')', ']', '}', '>'}

error_vals = {
	'(' : 1,
	'[' : 2,
	'{' : 3,
	'<' : 4
}

matching_1 = {
	')' : '(',
	']' : '[',
	'}' : '{',
	'>' : '<'
}

matching_2 = {
	'(' : ')',
	'[' : ']',
	'{' : '}',
	'<' : '>'
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
			if(matching_1[char] != stack.pop()):
				return 0;

	score = 0
	while(len(stack) != 0):
		item = stack.pop()
		score = (score*5) + error_vals[item]
	
	return score


arr = parce()
#print(arr)
allScores = list()
for line in arr:
	a = process_line(line)
	if(a != 0):
		allScores.append(a)

allScores.sort()
print(allScores)
print(len(allScores)//2)
print(allScores[len(allScores)//2])
#print(allScores[24])