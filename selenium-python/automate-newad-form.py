from common import *

try:
	filename = str(sys.argv[1])
except IndexError:
	print 'No input file'
	sys.exit(2)
	
if not os.path.isfile(filename):
	print 'Not a valid input file'
	sys.exit(2)

with open(filename) as data_file:	
	data = json.load(data_file)

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
		
	driver.quit()
