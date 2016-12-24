from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json, sys, getopt, os.path
import config as CONFIG

def get_driver():
	driver = webdriver.Chrome('/usr/local/bin/chromedriver')
	driver.get(CONFIG.NEWAD_URL)
	return driver
