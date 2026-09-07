# AirBnB Clone - The Console

## Description

This project is the first step of a larger AirBnB clone web application.
It implements a command interpreter (a shell, similar to Bash) used to
create, view, update, and delete the objects that make up the app —
starting with `BaseModel`, the parent class every other object type will
inherit from.

Objects are stored in memory and persisted to a JSON file
(`file.json`) through an abstracted storage engine (`FileStorage`), so
data survives between separate runs of the console.

## Environment

* Python 3.8.5
* Tested on Ubuntu 20.04 LTS
* pycodestyle 2.8.x compliant

## Command Interpreter

### How to start it

Run the console directly:

    $ ./console.py

Or explicitly with Python:

    $ python3 console.py

It also works in non-interactive mode, by piping commands in:

    $ echo "help" | ./console.py

### How to use it

Once started, you'll see the `(hbnb)` prompt. Available commands:

| Command   | Usage                                       | Description                                         |
|-----------|----------------------------------------------|------------------------------------------------------|
| `help`    | `help` or `help <command>`                    | Show available commands, or help for one command     |
| `quit`    | `quit`                                        | Exit the console                                      |
| `EOF`     | `Ctrl+D`                                      | Exit the console (end of file)                        |
| `create`  | `create <class>`                              | Create a new instance, save it, print its id           |
| `show`    | `show <class> <id>`                           | Print the string representation of an instance         |
| `destroy` | `destroy <class> <id>`                        | Delete an instance                                     |
| `all`     | `all` or `all <class>`                        | Print all instances, or all instances of one class      |
| `update`  | `update <class> <id> <attribute> "<value>"`   | Update an instance's attribute and save it              |

Currently supported classes: `BaseModel`

### Examples

Starting the console and getting help:

    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  create  destroy  help  quit  show  update

    (hbnb)

Creating a new instance:

    (hbnb) create BaseModel
    38f22813-2753-4d42-b37c-40a70a1a02f3

Showing an instance:

    (hbnb) show BaseModel 38f22813-2753-4d42-b37c-40a70a1a02f3
    [BaseModel] (38f22813-2753-4d42-b37c-40a70a1a02f3) {...}

Listing all instances:

    (hbnb) all BaseModel
    ["[BaseModel] (38f22813-2753-4d42-b37c-40a70a1a02f3) {...}"]

Updating an attribute:

    (hbnb) update BaseModel 38f22813-2753-4d42-b37c-40a70a1a02f3 name "My New Name"
    (hbnb) show BaseModel 38f22813-2753-4d42-b37c-40a70a1a02f3
    [BaseModel] (38f22813-2753-4d42-b37c-40a70a1a02f3) {..., 'name': 'My New Name'}

Deleting an instance:

    (hbnb) destroy BaseModel 38f22813-2753-4d42-b37c-40a70a1a02f3
    (hbnb) show BaseModel 38f22813-2753-4d42-b37c-40a70a1a02f3
    ** no instance found **

Exiting:

    (hbnb) quit
    $

## Running Tests

    $ python3 -m unittest discover tests

Or in non-interactive mode:

    $ echo "python3 -m unittest discover tests" | bash

## Authors

See [AUTHORS](AUTHORS)
