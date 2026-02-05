import sys

current_loc = None
dates = []

for line in sys.stdin:
    try:
        loc, date = line.strip().split('\t')
    except ValueError:
        continue

    if current_loc and loc != current_loc:
        dates.sort()
        for d in dates:
            print("{0}\t{1}".format(current_loc, d))
        dates = []

    current_loc = loc
    dates.append(date)

if current_loc:
    dates.sort()
    for d in dates:
        print("{0}\t{1}".format(current_loc, d))