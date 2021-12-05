#!/usr/env python3

with open("input.txt", 'r') as file:
	arr = file.readlines()
	counter = 0
	for i in range(len(arr)-3):
		A = int(arr[i][:-1]) + int(arr[i+1][:-1]) + int(arr[i+2][:-1])
		B = int(arr[i+1][:-1]) + int(arr[i+2][:-1]) + int(arr[i+3][:-1])
		if(A < B):
			counter += 1

	print(counter)