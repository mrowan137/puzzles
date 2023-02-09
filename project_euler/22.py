"""
Q: Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

A: 871198282
"""


class Name:
    def __init__(self, name):
        self.name_ = name

    def __call__(self):
        return self.name_

    def __eq__(self, other):
        return self.name_ == other.name_

    def __lt__(self, other):
        i, j = 0, 0
        while i < len(self.name_) and j < len(other.name_):
            if ord(self.name_[i]) < ord(other.name_[j]):
                return True
            elif ord(self.name_[i]) > ord(other.name_[j]):
                return False

            i += 1
            j += 1

        return False if i < len(self.name_) else True


def sum_of_name_scores():
    # read in the names and alphabetize
    file = open("names.txt", "r")
    names = file.readline().replace('"', "").split(",")
    file.close()
    names = [Name(name.strip()) for name in names]
    names = [name() for name in sorted(names)]

    # compute sum of name scores
    name_score = lambda name: sum(ord(c) - ord("A") + 1 for c in name)
    score = 0
    for i, name in enumerate(names):
        score += (i + 1) * name_score(name)

    return score


if __name__ == "__main__":
    print("Sum of name scores: {}".format(sum_of_name_scores()))
