import json, os.path, sys
from collections import OrderedDict
from quickstart import *
from common import print_usage
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
	row = column = ''
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

	def set_row(self, row):
		self.row = row
		self.rangeName = self.rangeName + row

	def set_column(self, column):
		self.column = column
		self.rangeName = self.rangeName + ':' + column

	def run_checks(self):
		if self.check_call_sheets_api():
			self.get_files_from_sheets_api() 
		else:
			temp = {}
			temp["config"] = self.local_config
			temp["input"] = self.local_input
			self.tests.append(temp)

	def check_call_sheets_api(self):
		if (self.row != "" and self.column == "") or (self.row == "" and self.column != ""):
			print 'Either column or row is missing'
			print_usage()
			sys.exit(2)
		elif self.row != "" and self.column != "":
			return True
		else:
			return False

	def get_files_from_sheets_api(self):
		files = call_sheets_api(self)
		for row in files:
			temp = {}
			temp["config"] = {}
			temp["input"] = []
			print 'row: {}'.format(row)
			for index, item in enumerate(row):
				if index == 0:
					print 'config: {}'.format(item)
					temp["config"] = self.set_config(item)
				else:
					print 'actions: {}'.format(item)
					temp["input"].append(self.set_input(item))

			self.tests.append(temp)
