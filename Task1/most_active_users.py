import re, os, operator
from collections import Counter


'''--------------reads data line by line from chats.txt-------------'''
def read(file):
	with open(file, "r") as f:
		data = f.readlines()  #read line by line
		#text = re.sub(r'^$\n', '', data, flags=re.MULTILINE)
		eof = f.tell() #reached end of file
		f.seek(0)
		if eof != f.tell():
			return data
		else:
			return None

'''--------------returns top 3 users from chat data-------------'''
def compute_active_users(data): 
	regex_pattern = r"<(.*)>" #matches names of people involved in chat
	names_list = []
	for line in data:
		match = re.match(regex_pattern, line)
		if match is not None: #ignore empty lines
			#print(match.group(1))
			names_list.append(match.group(1))

	#print(names_list) #names in chat to list
	counter=dict(Counter(names_list)) #dict containing names as keys and count as values

	sorted_counter = sorted(counter.items(), key=operator.itemgetter(1), reverse=True) #sort in descending to fetch top 3 active users
	#print(sorted_counter) 

	top3users = (sorted_counter[:3]) #fetch top 3 active users
	#print(top3users)

	most_active_users = []
	for x in top3users:
		most_active_users.append(x[0])

	return most_active_users 

'''----------Main Function---------'''
def main():
	filename = "chats.txt"
	contents = read(filename)
	result = compute_active_users(contents)
	print("Top 3 active users are:")
	for ele in result:
		print(ele)

if __name__ == '__main__':
	main()