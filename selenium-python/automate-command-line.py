from common import *
from collections import OrderedDict
import getopt
from data import *

def print_usage():
	print 'usage: python {} -c <configfile>.json -i <inputfile>.json'.format(__file__)
	sys.exit(2)

driver = []
def test2(data_obj):
	for data in data_obj.input:
		driver.append(get_driver(data_obj.url))
		for k,v in data.items():
			print k

			for index in range(0, data_obj.repeat):
				if k in 'assert':
					for i in v:
						print "Asserting %s in page" % (i["value"])
						assert str(i["value"]) in driver[index].page_source
				elif k in 'browser':
					driver[index].get(str(v[0]["url"]))
				else:
					for i in v:
						print 'i: ',i
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

	data_obj = Data()
	for opt, arg in opts:
		if opt == '-h':
			print_usage()
		elif opt in ("-c", "--config"):
			data_obj.set_config(arg)
		elif opt in ("-i", "--input"):
			data_obj.set_input(arg)

	test2(data_obj)


if __name__ == "__main__":
	main(sys.argv[1:])

