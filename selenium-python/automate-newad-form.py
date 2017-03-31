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
	elif k in 'assert':
		for i in v:
			print "Asserting %s in page" % (i["value"])
			assert str(i["value"]) in driver.page_source
	else:
		for i in v:
			attr = str(i["attr"])
			try:
				if (str(i["type"]) not in "image"):
					WebDriverWait(driver, 60).until(
						EC.element_to_be_clickable((getattr(By,	str(i["element"])), attr))
					)
			finally:
				print 'Did not find element'

			element = getattr(driver, 'find_element')(getattr(By, str(i["element"])), attr)
			if (str(i["type"]) == "dropdown"):
				select = Select(element)
				select.select_by_value(str(i["value"]))
			elif (str(i["type"]) in ["text", "image"]):
				if 'clear' in i:
					element.clear()
				element.send_keys(str(i["value"]))
			elif (str(i["type"]) in ["button","checkbox"]):
				if 'multiple' in i:
					list = getattr(driver, 'find_elements')(getattr(By, str(i["element"])), attr)
					list[int(i["multiple"])].click()
				else:
					element.click()
