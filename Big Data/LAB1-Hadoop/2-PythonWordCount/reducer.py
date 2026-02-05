#!/usr/bin/env python
import sys

current_word = None
current_count = 0
word = None

# Read each line from standard input
for line in sys.stdin:
    line = line.strip()

    # Parse the input we got from mapper.py
    try:
        word, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        # If the line is malformed, ignore it
        continue

    # Logic: If the word is the same as the previous one, add to count
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Write result to stdout
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# Output the last word if needed
if current_word == word:
    print('%s\t%s' % (current_word, current_count))