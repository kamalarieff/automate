from common import *

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
		data = json.load(data_file)
	except ValueError:
		print 'ERROR: Not a JSON file'
		print_usage()


for k,v in data.items():
	print k 
	driver = get_driver()
	for i in v:
		try:
			if (str(i["type"]) not in "image"):
				element = WebDriverWait(driver, 60).until(
					EC.element_to_be_clickable((By.ID, str(i["element_id"])))
				)
		finally:
			print 'Did not find element'

		if (str(i["type"]) == "dropdown"):
			select = Select(driver.find_element_by_id(str(i["element_id"])))
			select.select_by_value(str(i["value"]))
		elif (str(i["type"]) in ["text", "image"]):
			element = driver.find_element_by_id(str(i["element_id"]))
			element.send_keys(str(i["value"]))
		elif (str(i["type"]) == "button" or (str(i["type"]) == "checkbox" and str(i["value"]) == "1")):
			driver.find_element_by_id(str(i["element_id"])).click()
