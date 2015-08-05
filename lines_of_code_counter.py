#!/usr/bin/env python

# This Python script counts the lines of code in the directory in which it is
# run.  It only looks at files which end in the file extensions passed to the
# script as arguments.

# It outputs counts for total lines, blank lines, comment lines and code lines
# (total lines minus blank lines and comment lines).

# Example usage and output:
# > lines_of_code_counter.py .h .cpp
# Total lines:   15378
# Blank lines:   2945
# Comment lines: 1770
# Code lines:    10663

# Change this value based on the comment symbol used in your programming
# language.
commentSymbol = "//"

import sys
import os, os.path

acceptableFileExtensions = sys.argv[1:]
if not acceptableFileExtensions:
    print 'Please pass at least one file extension as an argument.'
    quit()

currentDir = os.getcwd()

filesToCheck = []
for root, _, files in os.walk(currentDir):
    for f in files:
        fullpath = os.path.join(root, f)
        if '.git' not in fullpath:
            for extension in acceptableFileExtensions:
            	if fullpath.endswith(extension):
                    filesToCheck.append(fullpath)

if not filesToCheck:
    print 'No files found.'
    quit()

totalLineCount = 0
blankLineCount = 0
commentLineCount = 0

for fileToCheck in filesToCheck:
    with open(fileToCheck) as f:
        for line in f:
            totalLineCount += 1
            lineWithoutWhitespace = line.strip()
            if not lineWithoutWhitespace:
                blankLineCount += 1
            elif lineWithoutWhitespace.startswith(commentSymbol):
                commentLineCount += 1

print 'Total lines:   ' + str(totalLineCount)
print 'Blank lines:   ' + str(blankLineCount)
print 'Comment lines: ' + str(commentLineCount)
print 'Code lines:    ' + str(totalLineCount - blankLineCount - commentLineCount)