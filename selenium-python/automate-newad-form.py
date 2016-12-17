from common import *
from test import input_params

driver = get_driver()

for i in input_params["inputs"]:
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
	elif (str(i["type"]) == "button"):
		driver.find_element_by_id(str(i["element_id"])).click()
		
# driver.quit()
