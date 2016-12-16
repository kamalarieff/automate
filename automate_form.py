import mechanize
# import ssl
# try:
# 	_create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
# 	# Legacy Python that doesn't verify HTTPS certificates by default
# 	pass
# else:
# 	# Handle target environment that doesn't support HTTPS verification
# 	ssl._create_default_https_context = _create_unverified_https_context
br = mechanize.Browser()
# br.set_all_readonly(False)	# allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders =		 [('User-allowgent', 'Firefox')]

br.open("https://www.google.com")
# for form in br.forms():
# 	print "Form name:", form.name
# 	print form

br.select_form('f')
br.form['q'] = 'foo'
response = br.submit()

print response
