#	       1  7  4  8
letters = {2, 3, 4, 7}

base_mapping = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"] 


def num_of_shared_chars(str1, str2):
	str1_set = set(str1)
	str2_set = set(str2)
	#print(len(str1_set.intersection(str2_set)))
	return len(str1_set.intersection(str2_set))


def find_mapping(inLine, base):
	found_mapping = [-1] * 10

	zero_six_nine_set = set()
	two_three_five_set = set()
	
	# first find knowns and remove them from set
	for item in inLine:
		item = ''.join(sorted(item))
		item_length = len(item)
		# is a 1
		if(item_length == 2):
			found_mapping[1] = item
		# is a 7
		elif(item_length == 3):
			found_mapping[7] = item
		# is a 4
		elif(item_length == 4):
			found_mapping[4] = item
		# is a 8
		elif(item_length == 7):
			found_mapping[8] = item
		# unknown rn

		# 0, 6, 9
		elif(len(item) == 6):
			zero_six_nine_set.add(item)
		# 2, 3, 5
		elif(len(item) == 5):
			two_three_five_set.add(item)

	'''
	temp_list = list(two_three_five_set)
	print(temp_list)
	# try the three cases to figure out three
	if(num_of_shared_chars(temp_list[0], temp_list[1]) == 3):
		# 3 is at index 2
		found_mapping[3] = temp_list[2]
	elif(num_of_shared_chars(temp_list[1], temp_list[2]) == 3):
		# 3 is at index 0
		found_mapping[3] = temp_list[0]
	elif(num_of_shared_chars(temp_list[0], temp_list[2]) == 3):
		# 3 is at index 1
		found_mapping[3] = temp_list[1]
	'''
	# find 6, 9 and 0
	for item in zero_six_nine_set:
		# found 9
		if(num_of_shared_chars(item, found_mapping[4]) == 4):
			found_mapping[9] = item
		# found 6, shares 3 chars with 3 and 1 with one
		elif(num_of_shared_chars(item, found_mapping[4]) == 3 and num_of_shared_chars(item, found_mapping[1]) == 1):
			found_mapping[6] = item
		# is zero
		else:
			found_mapping[0] = item

	# find 2, 3, 5
	for item in two_three_five_set:
		if(num_of_shared_chars(item, found_mapping[6]) == 5):
			found_mapping[5] = item
		elif(num_of_shared_chars(item, found_mapping[9]) == 4):
			found_mapping[2] = item
		else:
			found_mapping[3] = item



	return found_mapping



def parce(inputfile="input.txt"):
	with open(inputfile, 'r') as file:
		arr = file.readlines()
		outarr = list()
		results = list()
		for line in arr:
			allVals = line.replace(" |", "").replace("\n", "").split(" ")
			outarr.append(allVals)
			
			outVals = line.split("| ")[1].replace("\n", "").split(" ")
			results.append(outVals)
	return (outarr, results)


allVals, results = parce()
sum_all = 0
for i in range(len(results)):
	found_map = find_mapping(allVals[i], base_mapping)
	out_val = ''
	for j in range(len(results[i])):
		item = ''.join(sorted(results[i][j]))
		out_val += str(found_map.index(item))
	print(out_val)
	sum_all += int(out_val)
	
print(sum_all)