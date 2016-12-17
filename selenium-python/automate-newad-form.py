from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("http://regress.mudah.my:31004/ai/form/0?ca=9_s")
elem = driver.find_element_by_id("category_group")
all_options = elem.find_elements_by_tag_name("option")
for option in all_options:
	print("Value is: %s" % option.get_attribute("value"))
	option.click()
driver.close()
