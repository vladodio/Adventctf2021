#!/usr/bin/env python3

value = {
	"forward" : (1, 1, 0),
	"down" : (0, 0, 1),
	"up" : (0, 0, -1)
}



coords = [0,0,0]

with open("input.txt", 'r') as file:
	for line in file:
		parts = line.split(" ")

		mat = value[parts[0]]
		
		coords[2] += int(parts[1]) * mat[2]

		coords[0] += int(parts[1]) * mat[0]  
		coords[1] += int(parts[1]) * coords[2] * mat[1]

	print(coords[0] * coords[1])