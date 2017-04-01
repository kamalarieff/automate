import json, os.path, sys
from collections import OrderedDict
def print_usage():
	print 'usage: python {} -c <configfile>.json -i <inputfile>.json'.format(__file__)
	sys.exit(2)

class Data:
	def set_config(self, config):
		if not os.path.isfile(config):
			print 'ERROR: Not a file. JSON file needed'
			print_usage()

		with open(config) as config_file:
			try:
				data = json.load(config_file, object_pairs_hook=OrderedDict)
			except:
				print 'ERROR: Not a JSON file'
				print_usage()

			for k,v in data.items():
				print 'k: ', k
				print 'url: ', v[0]["url"]
				print 'repeat: ', v[0]["repeat"]
				Data.url = v[0]["url"]
				Data.repeat = v[0]["repeat"]
	
	def set_input(self, config):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
