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

## How to run

### Activate your virtualenv

```sh
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
