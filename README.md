## Getting started

### Required installations

#### chromedriver 2.26.436421
```sh
$ brew install chromedriver
```
* If chromedriver version is less, run
```sh
$ brew upgrade
```
#### selenium for python 3.0.2
```sh
$ sudo pip install selenium
```

## Input files

### Config

* url: The url you want to launch the browser with
* repeat: How many times you want to repeat the automation

### Assert

* value: Value you expect to be in the page

### Browser

* url: Redirect the browser to this url

### Automation

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

### Example

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
		"wait":"2",
		"type":"image",
		"element":"ID",
		"attr":"image_1",
		"value":"/Users/kamalarieff/Pictures/pp.jpeg"
	},
	{
		"wait":"2",
		"type":"text",
		"element":"ID",
		"attr":"subject",
		"value":"TEST FOR NEW JOB AI FORM"
	},
	{
		"type":"text",
		"element":"ID",
		"attr":"job_summary",
		"value":"TEST FOR NEW JOB AI FORM"
	},
	{
		"type":"text",
		"element":"ID",
		"attr":"education",
		"value":"TEST FOR NEW JOB AI FORM"
	},
	{
		"type":"dropdown",
		"element":"ID",
		"attr":"nationality",
		"value":"2"
	},
	{
		"type":"text",
		"element":"ID",
		"attr":"body",
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
		"attr":"language_skill",
		"value":"1",
		"multiple":"2"
	},
	{
		"type":"dropdown",
		"element":"ID",
		"attr":"gender_preferred",
		"value":"2"
	},
	{
		"type":"dropdown",
		"element":"ID",
		"attr":"own_transport",
		"value":"2"
	},
	{
		"type":"text",
		"element":"ID",
		"attr":"own_transport",
		"value":"TEST FOR NEW JOB AI FORM"
	},
	{
		"type":"checkbox",
		"element":"ID",
		"attr":"job_cat",
		"multiple":"0"
	},
	{
		"type":"checkbox",
		"element":"ID",
		"attr":"job_cat",
		"multiple":"4"
	},
	{
		"type":"checkbox",
		"element":"ID",
		"attr":"job_cat",
		"multiple":"9"
	},
	{
		"type":"dropdown",
		"element":"ID",
		"attr":"job_type",
		"value":"2"
	},
	{
		"type":"dropdown",
		"element":"ID",
		"attr":"contract_type",
		"value":"1"
	},
	{
		"type":"checkbox",
		"element":"ID",
		"attr":"experience_offer1"
	},
	{
		"type":"checkbox",
		"element":"ID",
		"attr":"experience_offer3"
	},
	{
		"type":"text",
		"element":"ID",
		"attr":"price_min",
		"value":"1000"
	},
	{
		"type":"text",
		"element":"ID",
		"attr":"price",
		"value":"3000"
	},
	{
		"type":"dropdown",
		"element":"ID",
		"attr":"salary_type",
		"value":"1"
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
		"type":"button",
		"element":"XPATH",
		"attr":"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a[text()='1']"
	},
	{
		"type":"dropdown",
		"element":"ID",
		"attr":"region",
		"value":"9"
	},
	{
		"type":"dropdown",
		"element":"ID",
		"attr":"area",
		"value":"397"
	},
	{
		"type":"text",
		"element":"ID",
		"attr":"company_name",
		"value":"Yoghirt Co"
	},
	{
		"type":"text",
		"element":"ID",
		"attr":"company_desc",
		"value":"Only the best is selled here"
	},
	{
		"type":"dropdown",
		"element":"ID",
		"attr":"company_size",
		"value":"7"
	},
	{
		"type":"text",
		"element":"ID",
		"attr":"company_roc",
		"value":"Kappa123"
	},
	{
		"type":"text",
		"element":"ID",
		"attr":"website",
		"value":"www.twitch.tv/admiralbulldog"
	},
	{
		"type":"text",
		"element":"ID",
		"attr":"resume_email_addr",
		"value":"ayylmao@gmail.com"
	},
	{
		"type":"button",
		"element":"ID",
		"attr":"preview_ad"
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

* Create a new json file with all the input params. See any files in the staging folder for example.

### Running the script

```sh
$ python automate-newad-form.py <inputfile>.json
```

## Helpful references

* https://github.com/dhruvramani/Terminal-on-FB-Messenger/issues/10
* http://stackoverflow.com/questions/8255929/running-webdriver-chrome-with-selenium/8259152#8259152
* http://selenium-python.readthedocs.io/installation.html
