from __future__ import print_function

f = open('temp2.json', 'r')
with open('temp2.json', 'r') as f:
	for line in f:
		if 'element_id' in line:
			num_tab = len(line) - len(line.lstrip('\t'))
			tab = '\t'*num_tab
			temp = tab+"\"element\":\"ID\","
			print (temp)
			line = line.replace("element_id","attr")
		print (line, end="")
