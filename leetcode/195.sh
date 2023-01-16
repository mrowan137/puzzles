"""
Runtime: 50 ms, faster than 29.72% of Bash online submissions for Tenth Line.
Memory Usage: 4 MB, less than 7.07% of Bash online submissions for Tenth Line.
"""
# Read from the file file.txt and output the tenth line to stdout.

# NR is AWK built in variable, number of records 
# can use NR in action block to get line number
# $0 is the whole line of arguments
awk '{if (NR==10) print $0}' file.txt
