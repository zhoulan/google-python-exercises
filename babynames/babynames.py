#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  f = open(filename, 'r')
  returnlist = []
  namesdict = {}
  for line in f:
    yearmatch = re.search(r'<h3 align="center">Popularity in ((\d){4})<\/h3>',line)
    if yearmatch:
      year = yearmatch.group(1)
      returnlist.append(year)
    namematch = re.search(r'<tr align="right"><td>(\d+)</td><td>([a-zA-Z]+)</td><td>([a-zA-Z]+)</td>', line)
    if namematch:
      if namematch.group(2) not in namesdict: #if already exist then the old index would be less
        namesdict[namematch.group(2)] = namematch.group(1)
      if namematch.group(3) not in namesdict:      
        namesdict[namematch.group(3)] = namematch.group(1)
  f.close()
  sorteddict = sorted(namesdict.items())
  returnlist.extend(sorteddict)
  return returnlist

def print_names(list):
  print list[0]
  for row in list[1:len(list)]:
    print row[0],row[1]

def write_to_summary_file(filename, list):
  outputfile = filename + '.summary'
  f = open(outputfile, 'w')
  content = str(list[0]) + "\n"
  for row in list[1:len(list)]:
    content += row[0] + " "+ row[1] + "\n"
  f.write(content)
  f.close()

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  nameslist = extract_names(args[0])
  if summary == True:
    write_to_summary_file(args[0], nameslist)
  else:
    print_names(nameslist)
  
  
if __name__ == '__main__':
  main()
