from common import *

driver = get_driver()

select = Select(driver.find_element_by_id("category_group"))
select.select_by_value("4180")

driver.implicitly_wait(10)

select = Select(driver.find_element_by_id("bag_type"))
select.select_by_value("1")

select = Select(driver.find_element_by_id("gender_type"))
select.select_by_value("1")

element = driver.find_element_by_id("subject")
element.send_keys("test using selenium subject 6")

element = driver.find_element_by_id("body")
element.send_keys("test using selenium body")

element = driver.find_element_by_id("price")
element.send_keys("123")

select = Select(driver.find_element_by_id("area"))
select.select_by_value("628")

element = driver.find_element_by_id("name")
element.send_keys("kamal")

element = driver.find_element_by_id("email")
element.send_keys("kamal.arieff@gmail.com")

element = driver.find_element_by_id("phone")
element.send_keys("0129500092")

element = driver.find_element_by_id("passwd")
element.send_keys("123123")

element = driver.find_element_by_id("passwd_ver")
element.send_keys("123123")

driver.find_element_by_id("c_publish").click()

try:
	element = WebDriverWait(driver, 100000).until(
		EC.element_to_be_clickable((By.ID, "photo-notification-btn-no"))
	)
finally:
	print 'Did not find element'

driver.find_element_by_id("photo-notification-btn-no").click()
driver.quit()
