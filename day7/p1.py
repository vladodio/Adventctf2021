def parce(inputfile="input.txt"):
	with open(inputfile, 'r') as file:
		arr = file.readlines()[0].split(",")
		outarr = list()
		for item in arr:
			outarr.append(int(item))
	return outarr



arr = parce()
outcomes = list()

# for each possible value
for i in range(max(arr)):
	avg = i
	total_fuel = 0
	for i in arr:
		total_fuel += abs(int(i)-avg)
	outcomes.append(total_fuel)

print(min(outcomes))