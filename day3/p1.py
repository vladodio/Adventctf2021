#!/usr/bin/env python3

leng = 12
line_num = 0



with open("input.txt", 'r') as file:
	arr = [0] * leng

	for line in file:
		line_num += 1
		for i in range(leng):
			if(line[i] == "1"):
				arr[i] += 1
	print(arr)

midpoint = line_num/2

print(midpoint)

for item in arr:
	if(item > midpoint):
		print(1, end='')
	else:
		print(0, end='')

print("")
