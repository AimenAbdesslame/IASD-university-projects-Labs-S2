import sys

# Loop through each line of input
for line in sys.stdin:
    # Remove leading/trailing whitespace
    line = line.strip()
    
    # Split the line into fields (assuming tab-separated)
    data = line.split('\t')

    # We expect 6 fields: date, time, store, item, cost, payment
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        
        # We only care about the Store and the Cost
        # Output: StoreName [tab] Cost
        print("{0}\t{1}".format(store, cost))