"""
Q: In the game, Monopoly, the standard board is set up in the following way:

     ___________________________________________
    |GO |A1 |CC1|A2 |T1 |R1 |B1 |CH1|B2 |B3 |JL |
    |___|___|___|___|___|___|___|___|___|___|___|
    |H2 |                                   |C1 |
    |___|                                   |___|
    |T2 |                                   |U1 |
    |___|                                   |___|
    |H1 |                                   |C2 |
    |___|                                   |___|
    |CH3|                                   |C3 |
    |___|                                   |___|
    |R4 |                                   |R2 |
    |___|                                   |___|
    |G3 |                                   |D1 |
    |___|                                   |___|
    |CC3|                                   |CC2|
    |___|                                   |___|
    |G2 |                                   |D2 |
    |___|                                   |___|
    |G1 |                                   |D3 |
    |___|___________________________________|___|
    |G2J|F3 |U2 |F2 |F1 |R3 |E3 |E2 |CH2|E1 |FP |
    |___|___|___|___|___|___|___|___|___|___|___|

A player starts on the GO square and adds the scores on two 6-sided dice to
determine the number of squares they advance in a clockwise direction. Without
any further rules we would expect to visit each square with equal probability:
2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH
(chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player
to go directly to jail, if a player rolls three consecutive doubles, they do not
advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player
lands on CC or CH they take a card from the top of the respective pile and,
after following the instructions, it is returned to the bottom of the pile.
There are sixteen cards in each pile, but for the purpose of this problem we are
only concerned with cards that order a movement; any instruction not concerned
with movement will be ignored and the player will remain on the CC/CH square.

  Community Chest (2/16 cards):
    1. Advance to GO
    2. Go to JAIL
  Chance (10/16 cards):
    1. Advance to GO
    2. Go to JAIL
    3. Go to C1
    4. Go to E3
    5. Go to H2
    6. Go to R1
    7. Go to next R (railway company)
    8. Go to next R
    9. Go to next U (utility company)
    10. Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular
square. That is, the probability of finishing at that square after a roll. For
this reason it should be clear that, with the exception of G2J for which the
probability of finishing on it is zero, the CH squares will have the lowest
probabilities, as 5/8 request a movement to another square, and it is the final
square that the player finishes at on each roll that we are interested in. We
shall make no distinction between "Just Visiting" and being sent to JAIL, and we
shall also ignore the rule about requiring a double to "get out of jail",
assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can
concatenate these two-digit numbers to produce strings that correspond with sets
of squares.

Statistically it can be shown that the three most popular squares, in order, are
JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So
these three most popular squares can be listed with the six-digit modal string:
102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the
six-digit modal string.


A: 101524
"""

import random


class Die:
    def __init__(self, faces):
        self.faces = faces
        self.last_3_rolls = []

    def roll(self):
        r = random.randint(1, self.faces)
        self.last_3_rolls.insert(0, r)
        if len(self.last_3_rolls) > 3:
            self.last_3_rolls.pop()

        return r

    def get_faces(self):
        return self.faces


class Monopoly:
    def __init__(self):
        # the die we roll for the game
        self.d1, self.d2 = Die(4), Die(4)

        # the board, 40 squares
        self.board_size = 40
        self.board = list(range(self.board_size))
        self.board_counter = {s: 0 for s in self.board}

        # start on go
        self.board_idx = 0
        self.board_counter[0] = 1

        # community chest cards; shuffled at start of game
        self.community_chest = [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "goto 00",
            "goto 10",
        ]
        random.shuffle(self.community_chest)
        self.community_chest_idx = 0
        self.community_chest_size = len(self.community_chest)

        # chance cards; shuffled at start of game
        self.chance = [
            "",
            "",
            "",
            "",
            "",
            "",
            "goto 00",
            "goto 10",
            "goto 11",
            "goto 24",
            "goto 39",
            "goto 05",
            "next rr",
            "next rr",
            "next uc",
            "back 3s",
        ]
        random.shuffle(self.chance)
        self.chance_idx = 0
        self.chance_size = len(self.chance)

    def advance(self, n):
        self.board_idx += n
        self.board_idx %= self.board_size

    def goto(self, place):
        self.board_idx = int(place)
        self.board_idx %= self.board_size

    def nxt(self, place):
        # advance to next railroad or utility
        if place == "rr":
            while self.board_idx not in [5, 15, 25, 35]:
                self.advance(1)
        elif place == "uc":
            while self.board_idx not in [12, 28]:
                self.advance(1)

    def record_visit(self):
        self.board_counter[self.board_idx] += 1

    def decode_instruction(self, instr):
        action, place = instr.split()
        return action, place

    def execute_instruction(self, instr):
        # make action based on pulled card
        if not instr:
            return

        action, place = self.decode_instruction(instr)

        # goto
        if action == "goto":
            self.goto(place)
        elif action == "next":
            self.nxt(place)
        elif action == "back":
            self.advance(-3)

    def draw(self, pile):
        if pile == "community chest":
            instruction = self.community_chest[self.community_chest_idx]
            self.community_chest_idx += 1
            self.community_chest_idx %= self.community_chest_size
        elif pile == "chance":
            instruction = self.chance[self.chance_idx]
            self.chance_idx += 1
            self.chance_idx %= self.chance_size

        return instruction

    def rolled_3_doubles(self):
        # there is a rule we need to go to jail if roll 3 doubles
        # so this is a check on that condition
        if len(self.d1.last_3_rolls) < 3:
            return False

        return all(
            self.d1.last_3_rolls[i] == self.d2.last_3_rolls[i] for i in range(3)
        )

    def play_a_turn(self):
        # roll the dice and advance
        r1, r2 = self.d1.roll(), self.d2.roll()
        self.advance(r1 + r2)

        # go to jail if we rolled 3 doubles
        if self.rolled_3_doubles():
            self.goto(10)

        # go to jail if we land go to jail
        if self.board_idx == 30:
            self.goto(10)

        # draw a card if we land a chance or community chest
        instruction = ""
        if self.board_idx in [7, 22, 36]:
            instruction = self.draw("chance")
        elif self.board_idx in [2, 17, 33]:
            instruction = self.draw("community chest")

        if instruction:
            self.execute_instruction(instruction)

        # log the square we end on
        self.record_visit()

    def play_n_turns(self, n):
        for _ in range(n):
            self.play_a_turn()

    def n_most_visited_squares(self, n):
        sorted_visited_squares = sorted(
            self.board_counter.keys(), key=lambda k: self.board_counter[k]
        )[::-1]
        return sorted_visited_squares[:n]


def main():
    game = Monopoly()
    game.play_n_turns(10000000)  # big enough for decent statistics
    answer = game.n_most_visited_squares(3)
    print(
        f"3 most visited squares (d1, d2 faces: {game.d1.faces}, {game.d2.faces}): {answer}"
    )


if __name__ == "__main__":
    main()
