from __future__ import print_function
import sys, os

def print_usage():
	print ('usage: python {} <inputfile>.json'.format(__file__))
	sys.exit(2)

def add_json_entry(w, line, element):
	num_tab = len(line) - len(line.lstrip('\t'))
	tab = '\t'*num_tab
	new_string = element.split('_')
	new_string = new_string[1].upper()
	temp = tab + "\"element\":\"" + new_string + "\",\n"
	w.write(temp)
	return line.replace(element,"attr")

try:
	filename = str(sys.argv[1])
except IndexError:
	print ('ERROR: No input file')
	print_usage()


w = open('temp.json', 'w')
with open(filename, 'r') as f:
	for line in f:
		if 'element_id' in line:
			line = add_json_entry(w,line, element = 'element_id')
		elif 'element_name' in line:
			line = add_json_entry(w,line, element = 'element_name')
		w.write(line)
	
os.rename('temp.json', filename)
