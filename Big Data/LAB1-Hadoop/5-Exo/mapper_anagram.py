import sys

# Read input line by line
for line in sys.stdin:
    # Remove whitespace and split the line into individual words
    line = line.strip()
    words = line.split()

    for word in words:
        # 1. Clean the word (optional: lowercase it to match correctly)
        clean_word = word.lower()
        
        # 2. Sort the characters to create the Key
        # "melon" -> ['e', 'l', 'm', 'n', 'o'] -> "elmno"
        sorted_key = "".join(sorted(clean_word))
        
        # 3. Output: SortedKey [tab] OriginalWord
        print("{0}\t{1}".format(sorted_key, clean_word))