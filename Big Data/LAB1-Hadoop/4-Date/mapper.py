import sys
import csv
import datetime

# Setup CSV reader to handle commas correctly
reader = csv.reader(sys.stdin)

def parse_date(date_str):
    # Tries to handle both m/d/yy and d/m/yy formats
    for fmt in ('%m/%d/%y', '%d/%m/%y', '%m/%d/%Y', '%d/%m/%Y'):
        try:
            return datetime.datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
    return None

for row in reader:
    # We need at least 4 columns (Location, Date, Year, Event_Type)
    if len(row) < 4:
        continue

    # --- UPDATED COLUMN NUMBERS ---
    location = row[0].strip()
    date_raw = row[1].strip()
    event_type = row[3].lower().strip()
    # ------------------------------

    # Filter: Look for events where territory was "regained"
    if "regains" in event_type:
        clean_date = parse_date(date_raw)
        
        if clean_date and location:
            print("{0}\t{1}".format(location, clean_date))