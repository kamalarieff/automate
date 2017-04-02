from __future__ import print_function
import sys, os

def print_usage():
	print ('usage: python {} <inputfile>.json'.format(__file__))
	sys.exit(2)

def add_json_entry(w, line, element, new_string):
	num_tab = len(line) - len(line.lstrip('\t'))
	tab = '\t'*num_tab
	temp = tab + "\"element\":\"" + new_string + "\",\n"
	w.write(temp)
	return line.replace(element,"attr")

try:
	filename = str(sys.argv[1])
except IndexError:
	print ('ERROR: No input file')
	print_usage()


w = open('temp.json', 'w')
config = False
with open(filename, 'r') as f:
	for line in f:
		if 'element_id' in line:
			line = add_json_entry(w,line, element = 'element_id', new_string = 'ID')
		elif 'element_name' in line:
			line = add_json_entry(w,line, element = 'element_name', new_string = 'NAME')
		elif 'element_class' in line:
			line = add_json_entry(w,line, element = 'element_class', new_string = 'CLASS_NAME')
		elif 'element_link' in line:
			line = add_json_entry(w,line, element = 'element_link', new_string = 'LINK_TEXT')
		elif 'element_xpath' in line:
			line = add_json_entry(w,line, element = 'element_xpath', new_string = 'XPATH')
		elif 'config' in line:
			config = True

		if config:
			if '],' in line:
				config = False
			line = ''
			

		w.write(line)
	
os.rename('temp.json', filename)
