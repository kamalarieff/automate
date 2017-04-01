from __future__ import print_function

w = open('test.json', 'w')
with open('staging/ai-cars-images-json', 'r') as f:
	for line in f:
		if 'element_id' in line:
			num_tab = len(line) - len(line.lstrip('\t'))
			tab = '\t'*num_tab
			temp = tab+"\"element\":\"ID\",\n"
			w.write(temp)
			line = line.replace("element_id","attr")
		w.write(line)
