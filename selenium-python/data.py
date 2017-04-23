import json, os.path, sys
from collections import OrderedDict
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
	def set_config(self, config):
		if not os.path.isfile(config):
			print 'ERROR: Not a file. JSON file needed'
			print_usage()

		with open(config) as config_file:
			data = check_json_file(config_file)

			for k,v in data.items():
				Data.url = v["url"]
				Data.repeat = int(v["repeat"]) if 'repeat' in v else 1
				Data.browser = v["browser"]
	
	def set_input(self, files):
		files = files.split(",")

		Data.input = []
		for i in files:
			with open(i) as input_file:
				data = check_json_file(input_file)
				Data.input.append(data)

			# print i
