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

r = br.open('https://regress.mudah.my:31011/controlpanel')
html = r.read()


# Show the available forms
# This is important
for f in br.forms():
	print f

br.select_form(nr=0)


br.form['username']='kamal'
br.form['cpasswd']='kamal'
br.submit()
print br.response().read()
