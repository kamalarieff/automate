def build_tests_list(data):
	temp = {}
	temp["config"] = data.local_config
	temp["input"] = data.local_input
	data.tests.append(temp)
