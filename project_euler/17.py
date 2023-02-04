"""
Q: If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.

A: 21124
"""

num_to_word_hundreds = {
    0: "",
    1: "one hundred",
    2: "two hundred",
    3: "three hundred",
    4: "four hundred",
    5: "five hundred",
    6: "six hundred",
    7: "seven hundred",
    8: "eight hundred",
    9: "nine hundred",
}

num_to_word_tens = {
    0: "",
    1: " and one",
    2: " and two",
    3: " and three",
    4: " and four",
    5: " and five",
    6: " and six",
    7: " and seven",
    8: " and eight",
    9: " and nine",
    10: " and ten",
    11: " and eleven",
    12: " and twelve",
    13: " and thirteen",
    14: " and fourteen",
    15: " and fifteen",
    16: " and sixteen",
    17: " and seventeen",
    18: " and eighteen",
    19: " and nineteen",
    20: " and twenty",
    21: " and twenty one",
    22: " and twenty two",
    23: " and twenty three",
    24: " and twenty four",
    25: " and twenty five",
    26: " and twenty six",
    27: " and twenty seven",
    28: " and twenty eight",
    29: " and twenty nine",
    30: " and thirty",
    31: " and thirty one",
    32: " and thirty two",
    33: " and thirty three",
    34: " and thirty four",
    35: " and thirty five",
    36: " and thirty six",
    37: " and thirty seven",
    38: " and thirty eight",
    39: " and thirty nine",
    40: " and forty",
    41: " and forty one",
    42: " and forty two",
    43: " and forty three",
    44: " and forty four",
    45: " and forty five",
    46: " and forty six",
    47: " and forty seven",
    48: " and forty eight",
    49: " and forty nine",
    50: " and fifty",
    51: " and fifty one",
    52: " and fifty two",
    53: " and fifty three",
    54: " and fifty four",
    55: " and fifty five",
    56: " and fifty six",
    57: " and fifty seven",
    58: " and fifty eight",
    59: " and fifty nine",
    60: " and sixty",
    61: " and sixty one",
    62: " and sixty two",
    63: " and sixty three",
    64: " and sixty four",
    65: " and sixty five",
    66: " and sixty six",
    67: " and sixty seven",
    68: " and sixty eight",
    69: " and sixty nine",
    70: " and seventy",
    71: " and seventy one",
    72: " and seventy two",
    73: " and seventy three",
    74: " and seventy four",
    75: " and seventy five",
    76: " and seventy six",
    77: " and seventy seven",
    78: " and seventy eight",
    79: " and seventy nine",
    80: " and eighty",
    81: " and eighty one",
    82: " and eighty two",
    83: " and eighty three",
    84: " and eighty four",
    85: " and eighty five",
    86: " and eighty six",
    87: " and eighty seven",
    88: " and eighty eight",
    89: " and eighty nine",
    90: " and ninety",
    91: " and ninety one",
    92: " and ninety two",
    93: " and ninety three",
    94: " and ninety four",
    95: " and ninety five",
    96: " and ninety six",
    97: " and ninety seven",
    98: " and ninety eight",
    99: " and ninety nine",
}


def count_letters_in_num(n):
    hundreds_part = n // 100
    tens_part = n % 100
    res = num_to_word_hundreds[hundreds_part] + num_to_word_tens[tens_part]
    if res[:4] == " and":
        res = res[4:]

    return len(res.replace(" ", ""))


def count_letters_in_num_up_to_1000():
    res = 0
    for i in range(1, 1000):
        res += count_letters_in_num(i)

    res += len("onethousand")
    return res


if __name__ == "__main__":
    print(
        "Count of letters in spelled-out numbers from 1 to 1000: {}".format(
            count_letters_in_num_up_to_1000()
        )
    )
