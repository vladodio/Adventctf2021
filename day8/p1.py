#	       1  7  4  8
letters = {2, 3, 4, 7}




def parce(inputfile="input.txt"):
	with open(inputfile, 'r') as file:
		arr = file.readlines()
		outarr = list()
		for line in arr:
			line = line.split("|")
			outarr.append(line[1].replace("\n", "").split(" "))
	return outarr

arr = parce()
#print(arr)

count = 0
for row in arr:
	for item in row:
		if(len(item) in letters):
			count += 1
print(count)

