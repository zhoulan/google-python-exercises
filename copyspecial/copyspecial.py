#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise

Part A (manipulating file paths).

Gather a list of the absolute paths of the special files in all the directories. In the simplest case, just print that list (here the "." after the command is a single argument indicating the current directory). Print one absolute path per line.

e.g. python copyspecial.py ../ ./


Part B (file copying)

If the "--todir dir" option is present at the start of the command line, do not print anything and instead copy the files to the given directory, creating it if necessary. Use the python module "shutil" for file copying.

e.g. python copyspecial.py --todir /Users/zhangzhoulan/Desktop/copyspecialtest/ .


Part C (calling an external program)

If the "--tozip zipfile" option is present at the start of the command line, run this command: "zip -j zipfile <list all the files>". This will create a zipfile containing the files. Just for fun/reassurance, also print the command line you are going to do first 

e.g. python copyspecial.py --tozip tem.zip .

"""
def get_special_path(dirname):
  returnlist = []
  for file in os.listdir(dirname):
    match = re.search(r'__(\w)+__',file)
    if match:
      returnlist.append(file)
  return returnlist

def copy_todir(todir, filelists):
  if not os.path.exists(todir):
    os.makedirs(todir)
  for file in filelists:
    shutil.copy(file, todir)
    
def zip_files(tozip, filelists):
  fileslists_string = " ".join(filelists)
  command = "zip -j " + tozip + " " + fileslists_string
  print "Command I'm going to do:" + command
  (status, output) = commands.getstatusoutput(command)
  if status:
    sys.stderr.write(output)
    sys.exit(1)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions  
  filelists = []
  for directory in args:
    dirlist = get_special_path(directory)  
    filelists.extend(dirlist)
    
  if todir == '' and tozip == '':
    for item in filelists:
      print item
  else:
    if todir != '':
      copy_todir(todir, filelists)
    else:
      zip_files(tozip, filelists)
  
  
if __name__ == "__main__":
  main()
