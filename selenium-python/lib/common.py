from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys, time
import config as CONFIG

def get_driver(url):
	driver = webdriver.Chrome('/usr/local/bin/chromedriver')
	driver.get(url)
	return driver

def print_usage():
	print 'usage: python {} -c <configfile>.json -i <inputfile>.json --row --column'.format(CONFIG.main_driver)
	sys.exit(2)

def run_actions(driver, input_data):
	for data in input_data:
		for k,v in data.items():
			if k in 'assert':
				for i in v:
					print "Asserting %s in page" % (i["value"])
					assert str(i["value"]) in driver.page_source
			elif k in 'browser':
				driver.get(str(v[0]["url"]))
			else:
				for i in v:
					print 'i: ',i
					if 'wait' in i:
						time.sleep(int(i["wait"]))
					attr = str(i["attr"])
					try:
						if (str(i["type"]) not in "image"):
							WebDriverWait(driver, 60).until(
								EC.element_to_be_clickable((getattr(By,	str(i["element"])), attr))
							)
					except:
						print 'Did not find element'

					element = getattr(driver, 'find_element')(getattr(By, str(i["element"])), attr)
					if (str(i["type"]) == "dropdown"):
						select = Select(element)
						select.select_by_value(str(i["value"]))
					elif (str(i["type"]) in ["text", "image"]):
						if 'clear' in i:
							element.clear()
						element.send_keys(str(i["value"]))
					elif (str(i["type"]) in ["button","checkbox","link"]):
						if 'multiple' in i:
							list = getattr(driver, 'find_elements')(getattr(By, str(i["element"])), attr)
							list[int(i["multiple"])].click()
						else:
							element.click()
