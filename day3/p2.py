#!/usr/bin/env python3

leng = 12
line_num = 0


def openFile(filename="input.txt"):
	outarr = []
	with open("input.txt", 'r') as file:
		for line in file:
				outarr.append(line)
	return outarr

# true in first param keeps more common
# false in first param keeps less common
def remove(removeType, arr, place):
	count = 0
	outarr1 = []
	outarr0 = []
	for i in arr:
		if("1" == i[place]):
			count += 1
			outarr1.append(i)
		else:
			count -= 1
			outarr0.append(i)

	if(removeType):
		if(count >= 0):
			return outarr1
		else:
			return outarr0
	else:
		if(count >= 0):
			return outarr0
		else:
			return outarr1

def co2(arr):
	place = 0
	while(len(arr) != 1):
		arr = remove(False, arr, place)
		place += 1
	return arr

def o2(arr):
	place = 0
	while(len(arr) != 1):
		arr = remove(True, arr, place)
		place += 1
	return arr

def main():
	arr = openFile()
	co2val = co2(arr)[0].replace("\n", "") 
	o2val = o2(arr)[0].replace("\n", "")

	co2val = int(co2val, 2)
	o2val = int(o2val, 2)

	print(co2val, o2val)
	print(co2val*o2val)



if __name__ == '__main__':
	main()