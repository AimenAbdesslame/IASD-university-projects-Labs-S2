import sys

current_key = None
anagram_list = []

for line in sys.stdin:
    # Parse input from mapper
    line = line.strip()
    try:
        key, word = line.split('\t')
    except ValueError:
        continue

    # If the key changes (new group of anagrams)
    if current_key and current_key != key:
        # Print the previous group
        print("{0}\t{1}".format(current_key, anagram_list))
        # Reset list for new key
        anagram_list = []

    current_key = key
    anagram_list.append(word)

# Print the final group
if current_key:
    print("{0}\t{1}".format(current_key, anagram_list))