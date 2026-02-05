#!/usr/bin/env python
import sys

# Read each line from standard input
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split the line into words
    words = line.split()
    # Output each word with a count of 1
    for word in words:
        print('%s\t%s' % (word, 1))