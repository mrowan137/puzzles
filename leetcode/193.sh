# Runtime: 126 ms, faster than 43.31% of Bash online submissions for Valid Phone Numbers.
# Memory Usage: 3.1 MB, less than 54.46% of Bash online submissions for Valid Phone Numbers.
# Read from the file file.txt and output all valid phone numbers to stdout.
grep -E '^[0-9]{3}-[0-9]{3}-[0-9]{4}$|^\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}$' file.txt
