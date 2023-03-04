"""
Q: The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?

A: 162
"""


def triangle_numbers(n):
    # compute triangle numbers <= n

    i, res = 1, []
    while True:
        tn = i * (i + 1) // 2
        if tn > n:
            break
        i += 1
        res.append(tn)

    return res


def is_triangle_word(w, triangle_nums):
    # is `w` a triangle word?
    v0 = ord("A") - 1
    v = sum([ord(c) - v0 for c in w])
    return v in triangle_nums


def count_triangle_words(file_name):
    # count triangle words in file `f`

    # read in the words
    words = []
    with open(file_name) as f:
        for line in f:
            line = line.replace('"', "")
            words += line.split(",")

    # find the longest word, biggest numeric value is 26*len(word)
    # and so we need to compute triangle numbers
    greatest_word_length = max([len(w) for w in words])
    triangle_nums = triangle_numbers(26 * greatest_word_length)

    cnt = 0
    for w in words:
        cnt += is_triangle_word(w, triangle_nums)

    return cnt


if __name__ == "__main__":
    f = "./words.txt"
    print(
        "Number of triangle words in file {}: {}".format(
            f, count_triangle_words(f)
        )
    )
