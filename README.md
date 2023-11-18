# 0x02. AirBnB clone - MySQL
This is a command-line interface that allows users to input commands, including any necessary arguments, to execute specific tasks. Users can create objects using this tool, manipulate existing objects, retrieve details about existing objects, and delete created objects.

This directory houses source code files for the AirBnB clone console project, showcasing enhanced and updated features compared to our [previous version](https://github.com/franklinobiukwu/AirBnB_clone)

## Features
This project serves as a command-line interpreter, empowering users to execute specified operations. The fundamental functionalities closely resemble [previous version](https://github.com/franklinobiukwu/AirBnB_clone) implementation details. Newer features include:
* Usage of MySQL to persist data

## Concepts
Concepts from [previous version](https://github.com/franklinobiukwu/AirBnB_clone) as well as:
* MySQL
* ORM
* SQLAlchemy
* Environment variables in Python

## Prerequisites
Additional tools needed alongside [previous version tools](https://github.com/franklinobiukwu/AirBnB_clone) include:
* SQLAlchemy [Download](https://pypi.org/project/SQLAlchemy/)
* MySQL 8.0 [Download](https://dev.mysql.com/downloads/installer/)
* MySQLdb [Download](https://stackoverflow.com/questions/25865270/how-to-install-python-mysqldb-module-using-pip)

## How-To Guide

## Launching the Command-Line Interpreter

Initiate the command-line tool from any terminal on a supported operating system using the provided snippet:

`./console.py`

This command starts the interactive mode, presenting a prompt for user input. The tool remains ready to process commands until the user opts to conclude the session.

To launch the tool in non-interactive mode, use the following snippet:

`echo "help" | ./console.py`

## Navigating the Command-Line Interpreter

Upon tool startup, perform a variety of operations directly from the command-line interface. Enter help to view a comprehensive list of available commands. For detailed information on the usage of any specific command, utilize the following snippet:

`help command_name`

## Usage Examples

```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
create  help	add  change  quit

Undocumented commands:
======================
(hbnb) help create
```
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```
Please note that the provided commands and examples are illustrative and should be adapted to fit your specific use case.
