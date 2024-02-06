# 0x00. AirBnB clone - The console
## Welcome to the AirBnB clone project!

## Project Overview:

This project aims to set up a simplified version of the AirBnB website on your server.
The first step involves creating a command-line tool in Python to store instance data in a JSON file. We use the `cmd` class for this purpose.
To ensure everything works smoothly, we've included unit tests using the Unittest framework.

## Resources
* [AirBnB clone](https://intranet.hbtn.io/concepts/74)
* [2 Airbnb console](https://www.youtube.com/watch?v=jeJwRB33YNg&feature=youtu.be)
* [HBNB project overview](https://www.youtube.com/watch?v=E12Xc3H2xqo&feature=youtu.be)
* [cmd module](https://docs.python.org/3.4/library/cmd.html)
* [packages](https://intranet.hbtn.io/concepts/66)
* [uuid module](https://docs.python.org/3.4/library/uuid.html)
* [datetime](https://docs.python.org/3.4/library/datetime.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args/kwargs](https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [HBNB - The console](https://www.youtube.com/watch?v=p00ES-5K4C8&feature=youtu.be)

## General

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Steps
You won’t build this application all at once, but step by step.

Each step will link to a concept:

##### The console:
* Create data model.
* CLI to manipulate objects.
* Storage engine abstraction (file storage engine).
##### Web static:
* Static HTML/CSS.
##### MySql:
* Add database storage engine.
##### Deploy Static:
* Deploy the application to go live!
##### Web Framework:
* Web server creation.
* Dynamic HTML.
##### RESTful API:
* Expose stored objects via JSON interface.
##### Web Dynamic:
* Using JQuery.
* Loading objects from client side.

### Execution

The console is started executing the file console.py in the main directory. From there now you are able to execute any command in the list of commands presented below. Here is a simple example of how the console works in interactive mode, and using the help command:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```

And also in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

```

## Tests :heavy_check_mark:

### 2. Unittests

All the files, classes, functions are tested with unit tests

```
python3 -m unittest discover tests
```

Unit tests also work in non-interactive mode:

```
echo "python3 -m unittest discover tests" | bash
```

## Technologies
#### Console (CLI) Technologies
* The console is written in Python version 3.4.3.
* The following coding style is verified by the PEP8 version 1.7.
* The console class HBNBCommand is based on the cmd python module.
* JSON to save data, serialize and deserialize it.
* Unittesting.

## Installation
* Clone the project on your PC
 ```sh
$ https://github.com/gitgitgitgit-hub-when-the-whistle-go/AirBnB_clone.git
```

## Getting Started
* Get into the directory
```sh
$ cd ./AirBnB_clone
```
* Start using the console (CLI)
```sh
$ ./console.py
```

## Copyright

Made by [**Chadi Boulahya**](https://github.com/gitgitgitgit-hub-when-the-whistle-go) & [**Soufiane Kamma**](https://github.com/SoufianKm) © 2024. All rights reserved.
