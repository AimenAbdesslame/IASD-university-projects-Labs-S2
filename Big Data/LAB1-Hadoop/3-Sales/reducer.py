import sys

sales_total = 0
old_key = None

for line in sys.stdin:
    data = line.strip().split("\t")
    
    # Ensure we have exactly 2 fields (Store, Cost)
    if len(data) != 2:
        continue

    this_key, this_sale = data

    try:
        this_sale = float(this_sale)
    except ValueError:
        # If the cost isn't a number, skip this line
        continue

    # If the store name changes, print the total for the previous store
    if old_key and old_key != this_key:
        print("{0}\t{1}".format(old_key, sales_total))
        sales_total = 0

    old_key = this_key
    sales_total += this_sale

# Print the final total for the last store
if old_key is not None:
    print("{0}\t{1}".format(old_key, sales_total))