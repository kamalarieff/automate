from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_driver():
	driver = webdriver.Chrome('/usr/local/bin/chromedriver')
	driver.get("http://regress.mudah.my:31004/ai/form/0?ca=9_s")
	return driver
