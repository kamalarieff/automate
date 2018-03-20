## Getting started

### Required installations

#### chromedriver
```sh
$ brew install chromedriver
```
* If chromedriver version is less or you may run into issues with it, run
```sh
$ brew upgrade chromedriver
```
#### selenium for python 3.0.2
```sh
$ sudo pip install selenium
```

#### phantomjs
```sh
$ brew install phantomjs
```

#### Google sheets API
```sh
$ pip install --upgrade google-api-python-client
```

## Input files

### Config

* url: The url you want to launch the browser with
* repeat: How many times you want to repeat the automation

#### Example

```javascript
{
	"config":[
	{
		"url":"http://www-schibstedclassifiedmedia.mudah.my",
		"repeat":"2"
	}
	]
}
```

### Assert

* value: Value you expect to be in the page

### Browser

* url: Redirect the browser to this url

### Actions

* wait: Time in seconds you want to wait. Can be used anytime e.g. before or after the element has been filled
* type: Type of the element
  * Possible values:
    1. text
    2. button
    3. link
    4. dropdown
    5. image
    6. checkbox
* element: [Selector of the element](http://selenium-python.readthedocs.io/api.html#locate-elements-by)
  * Possible values:
    1. ID
    2. NAME
    3. CLASS_NAME
    4. LINK_TEXT
    5. XPATH
* attr: Attribute of the element
* value: Value of the element
* multiple: Used for when multiple elements have the same id. First element starts with 0
* clear: Clear the element before inputting

#### Example

```javascript
{
	"1":[
	{
		"type":"link",
		"element":"LINK_TEXT",
		"attr":"INSERT AD"
	},
	{
		"type":"dropdown",
		"element":"ID",
		"attr":"category_group",
		"value":"7020"
	},
	{
		"wait":"2",
		"type":"image",
		"element":"ID",
		"attr":"image_0",
		"value":"/Users/kamalarieff/Pictures/pp.jpeg"
	},
	{
		"type":"text",
		"element":"ID",
		"attr":"job_summary",
		"value":"TEST FOR NEW JOB AI FORM"
	},
	{
		"type":"checkbox",
		"element":"ID",
		"attr":"language_skill",
		"value":"1",
		"multiple":"0"
	},
	{
		"type":"checkbox",
		"element":"ID",
		"attr":"experience_offer3"
	},
	{
		"type":"button",
		"element":"ID",
		"attr":"due_date"
	},
	{
		"type":"button",
		"element":"XPATH",
		"attr":"//span[text()='Next']"
	},
	{
		"type":"dropdown",
		"element":"ID",
		"attr":"region",
		"value":"9"
	}
	],
	"assert":[
	{
		"value":"jobsnew1@gmail.com"
	}
	],
	"browser":[
	{
		"url":"https://www.facebook.com"
	}
	]
}

```

## Converting from old format to new format

* If you have a lot of files with the old format, you can run the script to convert it to the new format

```sh
$ python modify_input_files.py <inputfile>.json
```

## How to run

### Activate your virtualenv

```sh A
$ source ~/virtualenv/bin/activate
```

* The path might be different on your system. It depends where you installed virtualenv

### Setup

#### Actions
* Create a new json file with all the input params. See any files in the actions folder for example.

#### Config
##### Browser
* Choose between three browsers (Chrome, Firefox, PhantomJS)
* Update the ``browser`` in ``lib/config.py``

### Running the script

#### Only one input file

```sh
$ python automate-command-line.py -c config_file.json -i input_file.json
```

#### More than one input files
##### Two ways to insert
1. Separate by commas

```$ python automate-command-line.py -c config_file.json -i input_file1.json,input_file2.json```

2. Multiple -i flags

```$ python automate-command-line.py -c config_file.json -i input_file1.json -i input_file2.json```

#### Google Sheets

##### General
* [It supports multiple rows fetched from sheets i.e. Ranges. You can find the spreadsheet ID and sheet ID here as well.](https://developers.google.com/sheets/api/guides/concepts)

##### Setup
* [You can follow the steps here to setup your environment](https://developers.google.com/sheets/api/quickstart/python)
  * From here, you will get `client_secret.json` file.
* Update your spreadsheet ID and sheet ID in ```lib/config.py```
* Your directory should look like this
  ```
    .
    ├── README.md
    ├── mechanize
    │   ├── automate_form.py
    │   └── forms
    └── selenium-python
        ├── actions
        ├── automate-command-line.py
        ├── client_secret.json
        ├── configs
        ├── drivers
        ├── lib
        ├── quickstart.py
        └── scripts
  ```
* Run this command to authenticate yourself to the Google Sheets API
  ```
  $ python quickstart.py
  ```
##### Command
```$ python automate-command-line.py --row=ROW --column=COLUMN```

##### Example
```$ python automate-command-line.py --row=A15 --column=C15```

## Helpful references

* [Exception AttributeError: "'Service' object has no attribute 'process'"](https://github.com/dhruvramani/Terminal-on-FB-Messenger/issues/10)
* [selenium.common.exceptions.WebDriverException: Message: 'ChromeDriver executable needs to be available in the path.](http://stackoverflow.com/questions/8255929/running-webdriver-chrome-with-selenium/8259152#8259152)
* [Selenium Python Docs](http://selenium-python.readthedocs.io/installation.html)
* [Sheets API](https://developers.google.com/sheets/api/)
