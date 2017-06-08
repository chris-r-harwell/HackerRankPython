#!/bin/env python3


import os


""" 

Faster in python3.

PEP 471 - os.scandir() function – a better and faster directory
iterator

PEP 471 adds a new directory iteration function, os.scandir(), to the
standard library. Additionally, os.walk() is now implemented using
scandir, which makes it 3 to 5 times faster on POSIX systems and 7 to
20 times faster on Windows systems. This is largely achieved by greatly
reducing the number of calls to os.stat() required to walk a directory
tree.

Additionally, scandir returns an iterator, as opposed to returning a list
of file names, which improves memory efficiency when iterating over very
large directories.

The following example shows a simple use of os.scandir() to display all
the files (excluding directories) in the given path that don’t start
with '.'. The entry.is_file() call will generally not make an additional
system call:

""" 
path = '.'  
for entry in os.scandir(path):
    if not entry.name.startswith('.') and entry.is_file():
        print(entry.name)

