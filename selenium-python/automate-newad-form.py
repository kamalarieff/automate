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
					if 'clear' in i:
						element.clear()
					element.send_keys(str(i["value"]))
				elif (str(i["type"]) == "button" or (str(i["type"]) == "checkbox" and str(i["value"]) == "1")):
					driver.find_element_by_id(str(i["element_id"])).click()
			elif 'element_name' in i:
				try:
					if (str(i["type"]) not in "image"):
						element = WebDriverWait(driver, 60).until(
							EC.element_to_be_clickable((By.NAME, str(i["element_name"])))
						)
				finally:
					print 'Did not find element'

				if (str(i["type"]) == "dropdown"):
					select = Select(driver.find_element_by_name(str(i["element_name"])))
					select.select_by_value(str(i["value"]))
				elif (str(i["type"]) in ["text", "image"]):
					element = driver.find_element_by_name(str(i["element_name"]))
					element.send_keys(str(i["value"]))
				elif (str(i["type"]) == "button" or (str(i["type"]) == "checkbox" and str(i["value"]) == "1")):
					driver.find_element_by_name(str(i["element_name"])).click()
			elif 'element_class' in i:
				if (str(i["type"]) == "dropdown"):
					select = Select(driver.find_element_by_class_name(str(i["element_class"])))
					select.select_by_value(str(i["value"]))
				elif (str(i["type"]) in ["text", "image"]):
					element = driver.find_element_by_class_name(str(i["element_class"]))
					element.send_keys(str(i["value"]))
				elif (str(i["type"]) == "button" or (str(i["type"]) == "checkbox" and str(i["value"]) == "1")):
					driver.find_element_by_class_name(str(i["element_class"])).click()
			elif 'element_link' in i:
				if (str(i["type"]) == "link"):
					if 'multiple' in i:
						list = driver.find_elements_by_link_text(str(i["element_link"]))
						list[int(i["multiple"])].click()
					else:
						driver.find_element_by_link_text(str(i["element_link"])).click()
