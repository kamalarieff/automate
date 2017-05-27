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
	input = []
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

			# print i
