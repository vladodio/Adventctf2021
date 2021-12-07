def parce(inputfile="input.txt"):
	with open(inputfile, 'r') as file:
		arr = file.readlines()[0].split(",")
		outarr = list()
		for item in arr:
			outarr.append(int(item))
	return outarr



arr = parce()
outcomes = list()

# for each possible alignment point
for i in range(max(arr)):
	avg = i
	total_fuel = 0
	for i in arr:
		total_fuel += sum(range(abs(int(i)-avg)+1))
	outcomes.append(total_fuel)

print(min(outcomes))