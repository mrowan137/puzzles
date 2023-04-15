"""
Q: For a number written in Roman numerals to be considered valid there are basic
rules which must be followed. Even though the rules allow some numbers to be
expressed in more than one way there is always a "best" way of writing a
particular number.

For example, it would appear that there are at least six ways of writing the
number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last
example is considered to be the most efficient, as it uses the least number of
numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'),
contains one thousand numbers written in valid, but not necessarily minimal,
Roman numerals; see About... Roman Numerals for the definitive rules for this
problem.

Find the number of characters saved by writing each of these in their minimal
form.

Note: You can assume that all the Roman numerals in the file contain no more
than four consecutive identical units.

A: 743
"""


def reduce_roman_numeral(roman_numeral):
    original = roman_numeral
    saved_chars = 0
    while True:
        old = saved_chars
        while roman_numeral.find("DCCCC") != -1:
            roman_numeral = roman_numeral.replace("DCCCC", "CM")
            saved_chars += 3
        while roman_numeral.find("CCCC") != -1:
            roman_numeral = roman_numeral.replace("CCCC", "CD")
            saved_chars += 2
        while roman_numeral.find("LXXXX") != -1:
            roman_numeral = roman_numeral.replace("LXXXX", "XC")
            saved_chars += 3
        while roman_numeral.find("XXXX") != -1:
            roman_numeral = roman_numeral.replace("XXXX", "XL")
            saved_chars += 2
        while roman_numeral.find("VIIII") != -1:
            roman_numeral = roman_numeral.replace("VIIII", "IX")
            saved_chars += 3
        while roman_numeral.find("IIII") != -1:
            roman_numeral = roman_numeral.replace("IIII", "IV")
            saved_chars += 2

        if old == saved_chars:
            print(
                "  {} ({})--> {} ({}) (savings {})".format(
                    original,
                    len(original),
                    roman_numeral,
                    len(roman_numeral),
                    saved_chars,
                )
            )
            return saved_chars


def roman_numerals(file_name):
    # read file
    roman_numerals = []
    with open(file_name) as f:
        for line in f:
            row = line.replace("\n", "")
            roman_numerals.append(row)

    res = 0
    # count saved characters by reducing each roman numeral
    for rn in roman_numerals:
        res += reduce_roman_numeral(rn)

    return res


if __name__ == "__main__":
    file_path = "./roman.txt"
    print(
        "Total saved characters by writing roman numerals concisely: {}".format(
            roman_numerals(file_path)
        )
    )
