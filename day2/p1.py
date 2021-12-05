#!/usr/bin/env python3

value = {
	"forward" : (1, 0),
	"down" : (0, 1),
	"up" : (0, -1)
}

with open("input.txt", 'r') as file:
	coords = [0,0]
	for line in file:
		parts = line.split(" ")

		mat = value[parts[0]]
		
		coords[0] += int(parts[1]) * mat[0] 
		coords[1] += int(parts[1]) * mat[1]
	print(coords[0] * coords[1])