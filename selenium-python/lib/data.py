import json, os.path, sys
from collections import OrderedDict
from quickstart import *
def print_usage():
	print 'usage: python {} -c <configfile>.json -i <inputfile>.json'.format(__file__)
	sys.exit(2)

def check_json_file(file):
	try:
		data = json.load(file, object_pairs_hook=OrderedDict)
	except:
		print 'ERROR: Not a JSON file'
		print_usage()
	return data

class Data:
	input = []
	rangeName = 'Sheet1!A'
	row = column = ''
	def set_config(self, config):
		if not os.path.isfile(config):
			print 'ERROR: Not a file. JSON file needed'
			print_usage()

		with open(config) as config_file:
			data = check_json_file(config_file)

			for k,v in data.items():
				Data.url = v[0]["url"]
				Data.repeat = int(v[0]["repeat"]) if 'repeat' in v[0] else 1
	
	def set_input(self, files):
		print files
		with open(files) as input_file:
			data = check_json_file(input_file)
			Data.input.append(data)

	def set_row(self, row):
		self.row = row
		self.rangeName = self.rangeName + row
		return self.rangeName

	def set_column(self, column):
		self.column = column
		self.rangeName = self.rangeName + ':' + column + self.row
		return self.rangeName

	def run_checks(self):
		if self.check_call_sheets_api():
			self.temp() 

	def check_call_sheets_api(self):
		if (self.row != "" and self.column == "") or (self.row == "" and self.column != ""):
			print 'Either column or row is missing'
			sys.exit(2)
		elif self.row != "" and self.column != "":
			return True
		else:
			return False

	def temp(self):
		files = test()
		print files
		for row in files:
			for index, item in enumerate(row):
				if index == 0:
					self.set_config(item)
				else:
					self.set_input(item)

	def temp1(self):
		print 'temp1'
