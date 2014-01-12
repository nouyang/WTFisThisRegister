WTFisThisRegister
=================

WTFisThisRegister is simply the Flask tutorial app
http://flask.pocoo.org/docs/tutorial/
with an two added functions: search and delete entries.

It was developed as a small dictionary app for displaying AVR documentation
in response to search queries. This arose in response to the fact that most of
the documentation for AVR is buried in datasheets that are hard to search and 
keep track of which pages are relevant to you.

In the future, hopefully this will turn into something closer to http://explainshell.com
instead. However, for the actual compilation of user-submitted documentation,
I have decided to switch to a wiki instead for the sake of getting something
useful by the end of Jan 2014: http://narwhaledu.com/AVRwiki

It may be seen online at http://salty-retreat-5363.herokuapp.com/.
![tdd](https://lh3.googleusercontent.com/-XMZGpXQ82bg/UtA-Aty4WYI/AAAAAAAA-Yc/O_31OAwdoVM/s912/Screenshot%2520from%25202014-01-10%252013%253A34%253A00.png)

Version
-----
0.1 Nyan?

Quickstart
-----
If you already have pip, virtualenv, and heroku:
```
$ git clone https://github.com/nouyang/WTFisThisRegister.git
$ cd WTFisThisRegister
$ virtualenv venv --distribute
$ source venv/bin/activate 
(venv)$ pip install -r requirements.txt
```

To run, either option below works:
```sh
(venv)$ python WTFisThisRegister.py 
(venv)$ foreman start
```
and go to localhost:5000 in your browser.

To deploy to heroku,
```sh
(venv)$ heroku create
(venv)$ git push heroku master 
(venv)$ heroku config:set SECRETKEY=123 USERNAME=admin PASSWORD=default
```
and go to the URL given in the shell output. It should be similar to
http://salty-retreat-5363.herokuapp.com/.

Note: You can generate a secretkey using python:
```python
$ python 
>>> import os, binascii
>>> binascii.hexlify(os.urandom(24))
```

Project Setup
-----
#### Download this repository from github.
```sh
$ git clone https://github.com/nouyang/WTFisThisRegister.git
```

#### Install Pip
Install pip, which is a [package management](http://en.wikipedia.org/wiki/Package_management_system) system for Python, similar to gem or npm for Ruby and Node, respectively. 

```sh
$ easy_install pip
```

#### Now install [virtualenv](https://pypi.python.org/pypi/virtualenv) to create an isolated environment for development. 

This is standard practice. Always, always, ALWAYS use virtualenv. If you don't, you will eventually run into problems with compatibility between different dependencies. Just do it.

```sh 
$ pip install virtualenv
```

#### Activate your virtualenv.

```sh
$ virtualenv venv --distribute --no-site-packages
$ source venv/bin/activate
```

> You know that you are in a virtual env, as the actual "env" is now show before the $ in your terminal - (env). To exit the virtual environment, use the command `deactivate`, then you can reactivate by navigating back to the directory and running - `source env/bin/activate`.

Note: --no-site-packages may not be needed, you will get a message saying
"The --no-site-packages flag is deprecated; it is now the default behavior."

Note: You should NOT have spaces in the path to this directory! Otherwise you
may encounter errors such as
```sh
Error [Errno 2] No such file or directory while executing command ".
```

#### Install dependencies.
This should be inside the virtualenv!

```sh
(venv)$ pip install -r requirements.txt 
```

Run Locally
-----
#### Configure local install
You need to create either a databaseconfig.py or a .env file (both is fine too).
You can use your favorite text editor to do so.
Examples of what are in the files are given below.

```sh
$ cat databaseconfig.py
secretkey = '1111'
username = 'admin'
password = 'default'
```

An example of what would go in .env if you are running this in a virtual
environment with foreman (as per the heroku tutorial):
```sh
$ cat .env
secrekey=1111
username=admin
password=default
```
Note the lack of spaces around the equals sign!
#### Run locally
To run, the first option is if you created a databaseconfig.py file, the second
if you created a .env file.
```sh
(venv)$ python WTFisThisRegister.py 
(venv)$ foreman start
```

Deploy on Heroku
------
We create a new heroku app, commit our files to it, and then set the
configuration variables.

```sh
(venv)$ heroku create --stack cedar
(venv)$ git commit heroku master
(venv)$ heroku config:set SECRETKEY=123 USERNAME=admin PASSWORD=default
```
Note: If you don't set the config variables, the app will still work, but it 
will be pretty useless since you can't login (it will flash a message, "Invalid
username", without crashing the app.

Note: You can generate a secretkey using python:
```
$ python 
>>> import os, binascii
>>> binascii.hexlify(os.urandom(24))
```

Remove from Heroku
------
```sh
$ heroku info
=== powerful-headland-6041
Git URL:       git@heroku.com:powerful-headland-6041.git
Owner Email:   blah@example.com 
Region:        us
Repo Size:     448k
Slug Size:     28M
Stack:         cedar
Tier:          Legacy
Web URL:       http://powerful-headland-6041.herokuapp.com/
$ heroku apps:destroy powerful-headland-6041 
```

Credits
-------
Some of the project setup documentation I borrowed from 
[https://github.com/mjhea0/flaskr-tdd]
