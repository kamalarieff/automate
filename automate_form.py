import mechanize
br = mechanize.Browser()
# br.set_all_readonly(False)	# allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders =		 [('User-allowgent', 'Firefox')]

r = br.open('http://google.com')
html = r.read()


# Show the available forms
for f in br.forms():
	print f

# Select the first (index zero) form
br.select_form(nr=0)

# Let's search
br.form['q']='weekend codes'
br.submit()
print br.response().read()

# Looking at some results in link format
for l in br.links(url_regex='stockrt'):
	print l
