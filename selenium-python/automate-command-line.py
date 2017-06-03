from collections import OrderedDict
import getopt,sys
from lib.common import *
from lib.data import *

driver = []
def run(data_obj):
	for test in data_obj.tests:
		for index in range(0, test["config"]["repeat"]):
			driver.append(get_driver(test["config"]["url"]))
			print 'driver: ', driver
			run_actions(driver[index], test["input"])

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hc:i:",["config=","input=","row=","column="])
	except IndexError:
		print 'ERROR: No input file'
		print_usage()
	except getopt.GetoptError:
		print 'Unsupported argument'
		print_usage()

	if len(opts) == 0:
		print_usage()

	data_obj = Data()
	for opt, arg in opts:
		if opt == '-h':
			print_usage()
		elif opt in ("-c", "--config"):
			data_obj.set_config(arg)
		elif opt in ("-i", "--input"):
			if ',' in arg:
				arg = arg.split(",")
				for i in arg:
					data_obj.set_input(i)
			else:
				data_obj.set_input(arg)
		elif opt in ("--row"):
			data_obj.set_row(arg)
		elif opt in ("--column"):
			data_obj.set_column(arg)

	data_obj.run_checks()
	# for i in data_obj.tests:
	# 	print 'i: ', i

	print 'url: ', data_obj.tests[0]["config"]["url"]
	print 'repeat: ', data_obj.tests[0]["config"]["repeat"]
	print 'input: ', data_obj.tests[0]["input"][0]
	# print data_obj.tests[1] = input
	# print data_obj.tests[0].keys()
	# print data_obj.tests[1].values()
	# print iter(data_obj.tests[0])

	run(data_obj)

if __name__ == "__main__":

	main(sys.argv[1:])
