from timeit import default_timer as timer

'''
Write a function that given a list of strings and an input string will return True if you can create
the input string from the list of strings and will return False if you cannot create the string from
the list.
Example:
Function: ​can_create(list_of_strings, input_string)
List_of_strings = [‘back’, ‘end’, ‘front’, ‘tree’]
Input_string = ‘backend’ ---> Function returns True
Input_string = ‘frontyard’ ----> function returns False
Input_string = ‘frontend’ ---> function returns True
'''

# Naive approach-
start = timer()
def can_create1(l = None, i = None):
	'''generate all permutations of words from list of strings and find result'''
	
	global_list = []

	if l is None or i is None:
		return False

	for ele in l:
		sudo = ele #first combination
		for ele in l:
			if ele is not sudo:
				new_combination = sudo + ele
				global_list.append(new_combination)
	global_list = list(set(global_list))
	#print(global_list)
	if i in global_list:
		return True
	else:
		return False

end = timer() 
#print("%.25f"%(end - start))


# DP Approach-
start = timer()
def can_create2(l = None, i = None):

	'''
	1. find one part of input_string and check if its in input list.
	2. if in input list
		2.1 set True
		2.2 find next part of input_string  and check if its in input list.
		2.3 if in input list
				return true
			else 
				return false
	'''

	if l is None or i is None:
		return False

	n = len(i)
	global_list = [False] * n #initialise boolean list with False

	if n == 0 or i in l:
		global_list[0] = True
		return True

	for x in range(0, len(i)):
		if not global_list[x] and i[0 : x+1] in l: #edge case 1
			global_list[x] = True

		if global_list[x] == True and x == (len(i) - 1): #edge case 2
			return True

		#once we encounter 1 True (i.e. first half of word in list), check for second half
		if global_list[x] == True:
			for y in range(x+1, len(i)): 
				if global_list[y] == False and (i[x+1 : y+1] in l):
					global_list[y] = True

				if y == len(i) - 1 and global_list[y]:
					return True
	return global_list[len(i) - 1]

end = timer()
#print("%.25f"%(end - start))

if __name__ == '__main__':
	list_of_strings = ['back', 'end', 'front', 'tree']
	input_string = 'frontyard'
	print(can_create1(list_of_strings, input_string))
	print(can_create2(list_of_strings, input_string))