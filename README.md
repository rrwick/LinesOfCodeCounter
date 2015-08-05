# Lines of code counter

This Python script counts the lines of code in the directory in which it is run.  It only looks at files which end in the file extensions passed to the script as arguments.

It outputs counts for total lines, blank lines, comment lines and code lines (total lines minus blank lines and comment lines).

Example usage and output:

```
> lines_of_code_counter.py .h .cpp
Total lines:   15378
Blank lines:   2945
Comment lines: 1770
Code lines:    10663
```

License: GNU General Public License, version 3
