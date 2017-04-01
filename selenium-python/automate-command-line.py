from common import *
from collections import OrderedDict
import getopt

def print_usage():
	print 'usage: python {} -c <configfile>.json -i <inputfile>.json'.format(__file__)
	sys.exit(2)

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hc:i:",["config=","input="])
	except IndexError:
		print 'ERROR: No input file'
		print_usage()
	except getopt.GetoptError:
		print 'Unsupported argument'
		print_usage()

	if len(opts) == 0:
		print_usage()

	for opt, arg in opts:
		if opt == '-h':
			print_usage()
		elif opt in ("-c", "--config"):
			config = arg
			print 'Config file is ', config
		elif opt in ("-i", "--input"):
			files = arg.split(",")
			print 'Input file is ', files

	test(config, files)

def test(config, filename):
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
			# repeat = int(v[0]["repeat"]) if 'repeat' in v[0] else 1
			# driver = []

def test1():
	with open(filename) as data_file:
		try:
			data = json.load(data_file, object_pairs_hook=OrderedDict)
		except ValueError:
			print 'ERROR: Not a JSON file'
			print_usage()

	for k,v in data.items():
		print k 
		if k in "config":
			repeat = int(v[0]["repeat"]) if 'repeat' in v[0] else 1
			driver = []

		for index in range(0, repeat):
			if k in "config":
				driver.append(get_driver(v[0]["url"]))
			elif k in 'assert':
				for i in v:
					print "Asserting %s in page" % (i["value"])
					assert str(i["value"]) in driver[index].page_source
			elif k in 'browser':
				driver[index].get(str(v[0]["url"]))
			else:
				for i in v:
					if 'wait' in i:
						time.sleep(int(i["wait"]))
					attr = str(i["attr"])
					try:
						if (str(i["type"]) not in "image"):
							WebDriverWait(driver[index], 60).until(
								EC.element_to_be_clickable((getattr(By,	str(i["element"])), attr))
							)
					except:
						print 'Did not find element'

					element = getattr(driver[index], 'find_element')(getattr(By, str(i["element"])), attr)
					if (str(i["type"]) == "dropdown"):
						select = Select(element)
						select.select_by_value(str(i["value"]))
					elif (str(i["type"]) in ["text", "image"]):
						if 'clear' in i:
							element.clear()
						element.send_keys(str(i["value"]))
					elif (str(i["type"]) in ["button","checkbox","link"]):
						if 'multiple' in i:
							list = getattr(driver[index], 'find_elements')(getattr(By, str(i["element"])), attr)
							list[int(i["multiple"])].click()
						else:
							element.click()

if __name__ == "__main__":
	main(sys.argv[1:])
