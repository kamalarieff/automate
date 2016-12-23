from common import *
from test import input_params
import json

with open('test.json') as data_file:    
    data = json.load(data_file)

for k,v in data.items():
	print k 
	driver = get_driver()
	for i in v:
		try:
			element = WebDriverWait(driver, 10).until(
				EC.element_to_be_clickable((By.ID, str(i["element_id"])))
			)
		finally:
			print 'Did not find element'

		if (str(i["type"]) == "dropdown"):
			select = Select(driver.find_element_by_id(str(i["element_id"])))
			select.select_by_value(str(i["value"]))
		elif (str(i["type"]) == "text"):
			element = driver.find_element_by_id(str(i["element_id"]))
			element.send_keys(str(i["value"]))
		elif (str(i["type"]) == "button" or (str(i["type"]) == "checkbox" and str(i["value"]) == "1")):
			driver.find_element_by_id(str(i["element_id"])).click()
		
	# driver.quit()
