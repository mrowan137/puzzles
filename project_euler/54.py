"""
Q: In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

A: 376
"""

from collections import Counter


class Hand:
    def __init__(self, cards):
        # cards is expected in the format:
        #   [c_1, c_2, c_3, c_4, c_5]
        # where c_i (card i) is the ith card in format '<rank><suit>'

        # name of the hand
        self.cards = cards
        (
            self.hand_name,
            self.hand_score,
            self.rank_cards,
            self.nonrank_cards,
        ) = self.cards_to_kind(cards)

    def cards_to_kind(self, cards):
        # convert rank to integer
        rank_to_score = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }

        ranks = sorted([rank_to_score[c[0]] for c in cards])
        suits = [c[1] for c in cards]
        self.ranks, self.suits = ranks, suits

        ranks_count = Counter(ranks)
        ranks_count_count = Counter(ranks_count.values())

        # return is: hand name, hand score, rank card ranks, nonrank card ranks
        if ranks == [10, 11, 12, 13, 14] and len(set(suits)) == 1:
            rank_cards, nonrank_cards = ranks, []
            return "royal flush", 0, rank_cards, nonrank_cards
        elif (
            [r - min(ranks) for r in ranks] == [0, 1, 2, 3, 4]
            or [r - min(ranks) for r in ranks] == [0, 1, 2, 3, 12]
        ) and len(set(suits)) == 1:
            rank_cards, nonrank_cards = ranks, []
            return "straight flush", -1, rank_cards, nonrank_cards
        elif 4 in ranks_count.values():
            rank_cards = [r for r in ranks if ranks_count[r] == 4]
            nonrank_cards = [r for r in ranks if ranks_count[r] != 4]
            return "four of a kind", -2, rank_cards, nonrank_cards
        elif 3 in ranks_count.values() and 2 in ranks_count.values():
            rank_cards, nonrank_cards = ranks, []
            return "full house", -3, rank_cards, nonrank_cards
        elif len(set(suits)) == 1:
            rank_cards, nonrank_cards = ranks, []
            return "flush", -4, rank_cards, nonrank_cards
        elif [r - min(ranks) for r in ranks] == [0, 1, 2, 3, 4] or [
            r - min(ranks) for r in ranks
        ] == [0, 1, 2, 3, 13]:
            rank_cards, nonrank_cards = ranks, []
            return "straight", -5, rank_cards, nonrank_cards
        elif 3 in ranks_count.values():
            rank_cards = [r for r in ranks if ranks_count[r] == 3]
            nonrank_cards = [r for r in ranks if ranks_count[r] != 3]
            return "three of a kind", -6, rank_cards, nonrank_cards
        elif ranks_count_count[2] == 2:
            rank_cards = [r for r in ranks if ranks_count[r] == 2]
            nonrank_cards = [r for r in ranks if ranks_count[r] != 2]
            return "two pairs", -7, rank_cards, nonrank_cards
        elif ranks_count_count[2] == 1:
            rank_cards = [r for r in ranks if ranks_count[r] == 2]
            nonrank_cards = [r for r in ranks if ranks_count[r] != 2]
            return "one pair", -8, rank_cards, nonrank_cards
        else:
            rank_cards = [r for r in ranks if r == max(ranks_count)]
            nonrank_cards = [r for r in ranks if r != max(ranks_count)]
            return "high card", -9, rank_cards, nonrank_cards

    def __eq__(self, other):
        return self.ranks == other.ranks and self.suits == other.suits

    def __lt__(self, other):
        if self.hand_score == other.hand_score:
            # tiebreaker
            i = len(self.rank_cards) - 1
            while i >= 0 and self.rank_cards[i] == other.rank_cards[i]:
                i -= 1

            if i >= 0:
                # resolution from ranked cards
                return self.rank_cards[i] < other.rank_cards[i]

            i = len(self.nonrank_cards) - 1
            while self.nonrank_cards[i] == other.nonrank_cards[i]:
                i -= 1

            # ranked cards tie, resolution from nonrank cards
            return self.nonrank_cards[i] < other.nonrank_cards[i]

        return self.hand_score < other.hand_score


def poker(file_name):
    # read file
    cards = []
    with open(file_name) as f:
        for line in f:
            p1p2 = line.replace("\n", "").split(" ")
            cards.append(p1p2)

    res = 0
    for i, p1p2_hands in enumerate(cards):
        p1, p2 = Hand(p1p2_hands[0:5]), Hand(p1p2_hands[5:10])
        print(
            "hand {}\n".format(i + 1)
            + "--------\n"
            + "  P1 {} ({})\n".format(p1.cards, p1.hand_name)
            + "  P2 {} ({})\n".format(p2.cards, p2.hand_name)
            + "  Winner: {}\n".format("P1" if p1 > p2 else "P2")
        )
        res += p1 > p2

    return res


if __name__ == "__main__":
    print("P1 winning hands: {}".format(poker("./poker.txt")))
