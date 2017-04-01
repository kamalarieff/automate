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

* Change your url in common.py
* Create a new json file with all the input params. See springcleaning.json for example.

### Running the script

```sh
$ python automate-newad-form.py <inputfile>.json
```

## Helpful references

* https://github.com/dhruvramani/Terminal-on-FB-Messenger/issues/10
* http://stackoverflow.com/questions/8255929/running-webdriver-chrome-with-selenium/8259152#8259152
* http://selenium-python.readthedocs.io/installation.html
