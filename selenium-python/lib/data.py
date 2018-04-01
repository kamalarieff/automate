import json, os.path, sys
from collections import OrderedDict
from common import print_usage
from config import SHEET_ID
import sheets as Sheet
import local as Local
def check_json_file(file):
	try:
		data = json.load(file, object_pairs_hook=OrderedDict)
	except:
		print 'ERROR: Not a JSON file'
		print_usage()
	return data

class Data:
	tests = []
	local_input = []
	local_config = {}
	rangeName = SHEET_ID
	start_cell = end_cell = ''
	def set_config(self, config):
		if not os.path.isfile(config):
			print 'ERROR: Not a file. JSON file needed'
			print_usage()

		temp = {}

		with open(config) as config_file:
			data = check_json_file(config_file)

			for k,v in data.items():
				temp["url"] = v[0]["url"]
				temp["repeat"] = int(v[0]["repeat"]) if 'repeat' in v[0] else 1

		self.local_config = temp
		return temp
	
	def set_input(self, files):
		print files

		with open(files) as input_file:
			data = check_json_file(input_file)

		self.local_input.append(data)
		return data

	def set_start_cell(self, start_cell):
		self.start_cell = start_cell
		self.rangeName = self.rangeName + start_cell

	def set_end_cell(self, end_cell):
		self.end_cell = end_cell
		self.rangeName = self.rangeName + ':' + end_cell

	def run_checks(self):
		if self.check_call_sheets_api():
			files = self.get_files_from_sheets_api() 
		else:
			files = None
		self.build_tests_list(files)

	def build_tests_list(self, files=None):
		if files:
			Sheet.build_tests_list(self, files)
		else:
			Local.build_tests_list(self)

	def check_call_sheets_api(self):
		if (self.start_cell != "" and self.end_cell == "") or (self.start_cell == "" and self.end_cell != ""):
			print 'Either start_cell or end_cell is missing'
			print_usage()
			sys.exit(2)
		elif self.start_cell != "" and self.end_cell != "":
			return True
		else:
			return False

	def get_files_from_sheets_api(self):
		return Sheet.call_sheets_api(self)
