import mechanize
import ssl
try:
	_create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
	# Legacy Python that doesn't verify HTTPS certificates by default
	pass
else:
	# Handle target environment that doesn't support HTTPS verification
	ssl._create_default_https_context = _create_unverified_https_context
br = mechanize.Browser()
# br.set_all_readonly(False)	# allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders =		 [('User-allowgent', 'Firefox')]

r = br.open('http://regress.mudah.my:31004/ai/form/1?ca=9_s&tpl=0')
html = r.read()

br.select_form(nr=0)

br.form['category_group']=['4180',]
br.form['type']=['s',]
br.form['region']=['12',]
br.form['subarea']=['628',]
br.form['name']='kamal'
br.form['bag_type']=['1',]
br.submit()
print br.response().read()
