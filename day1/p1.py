#!/usr/env python3

with open("input.txt", 'r') as file:
	arr = file.readlines()
	counter = 0
	for i in range(len(arr)-1):
		if(int(arr[i][:-1]) < int(arr[i+1][:-1])):
			counter += 1
		else:
			print(f'{arr[i][:-1]} > {arr[i+1][:-1]}')
	print(counter)