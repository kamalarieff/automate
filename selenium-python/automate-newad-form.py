from common import *
from collections import OrderedDict

def print_usage():
	print 'usage: python {} <inputfile>.json'.format(__file__)
	sys.exit(2)

try:
	filename = str(sys.argv[1])
except IndexError:
	print 'ERROR: No input file'
	print_usage()
	
if not os.path.isfile(filename):
	print 'ERROR: Not a file. JSON file needed'
	print_usage()

with open(filename) as data_file:	
	try:
		data = json.load(data_file, object_pairs_hook=OrderedDict)
	except ValueError:
		print 'ERROR: Not a JSON file'
		print_usage()


for k,v in data.items():
	print k 
	if k in "config":
		driver = get_driver(v[0]["url"])
	else:
		for i in v:
			if 'element_id' in i:
				temp = 'element_id'.split("_")
				if (str(i["type"]) in ["text", "image"]):
					temp1 = 'find_element_by_'+ temp[1]
					element = getattr(driver, temp1)(str(i["element_id"]))
					if 'clear' in i:
						element.clear()
					element.send_keys(str(i["value"]))
			if 'element_name' in i:
				element = str(i["element_name"])
				try:
					if (str(i["type"]) not in "image"):
						WebDriverWait(driver, 60).until(
							EC.element_to_be_clickable((By.NAME, element))
						)
				finally:
					print 'Did not find element'
				temp = 'element_name'.split("_")
				if (str(i["type"]) in ["text", "image"]):
					temp1 = 'find_element_by_'+ temp[1]
					element = getattr(driver, temp1)(element)
					element.send_keys(str(i["value"]))
