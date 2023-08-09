"""
Q: If a box contains twenty-one coloured discs, composed of fifteen blue discs
and six red discs, and two discs were taken at random, it can be seen that the
probability of taking two blue discs, P(BB) = (15/21)*(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two
blue discs at random, is a box containing eighty-five blue discs and thirty-five
red discs.

By finding the first arrangement to contain over 10^12 = 1 000 000 000 000 discs
in total, determine the number of blue discs that the box would contain.

A: 756872327473
"""


#  Solving the eqs.:
#    1) r + b = N
#
#    2)   b       b - 1     1
#       ----- * --------- = -
#       r + b   r + b - 1   2
#
#  yields:
#
#    b = 0.5*( 1 + sqrt(2*N^2 - 2*N + 1) )
#
#  Look for a pattern (`numerology' approach):
#
#  N (total)       b (blue)       N_i / N_{i - 1}
#  -------------   -----------    ----------------
#  21              15
#  120             85             5.71428571428571
#  697             493            5.80833333333333
#  4060            2871           5.82496413199426
#  23661           16731          5.82783251231527
#  137904          97513          5.82832509192342
#  803761          568345         5.82840961828518
#  4684660         3312555        5.82842412110068
#  27304197        19306983       5.82842660940175
#  159140520       112529341      5.82842703632705
#  927538921       655869061      5.82885418144767
#  5406093004      3822685023     5.82842712214337
#  31509019101     22280241075    5.82842712429962
#  183648021600    129858761425   5.82842712466957
#  1070379110497   756872327473   5.82842712473304
#
#  It seems, within the samples considered, around a factor ~5.828x (as an
#  underestimate) for successive values N_i. We can continue use the ratio
#  N_i/N_{i-1} to make a slight underestimate of N_{i+1}, i.e.
#  N_{i+1} ~= N_{i}*N_{i}/N_{i-1}. Then linear search to get the solution.


from decimal import Decimal


def residual(N):
    # return the difference 2*b*(b-1) - N*(N-1),
    # coming from 1/2 == (b/N)*(b-1)/(N-1)
    b = int(
        Decimal(0.5)
        * (
            Decimal(1)
            + (
                Decimal(2) * Decimal(N) ** 2
                - Decimal(2) * Decimal(N)
                + Decimal(1)
            ).sqrt()
        )
    )
    t1, t2 = Decimal(2) * Decimal(b) * (Decimal(b) - Decimal(1)), Decimal(N) * (
        Decimal(N) - Decimal(1)
    )
    return t1 - t2, b


def arranged_probability(N0):
    # linear search for a solution to p(BB) == 1/2, starting from N0 discs
    N = N0

    while True:
        res, b = residual(N)
        if res == 0:
            break

        N += 1

    return N, b


if __name__ == "__main__":
    # initial estimate with simple calculation using table above:
    #   x0, f = 183648021600, 5.82842712466957
    #   x = x0
    #   while x < 1e12: x *= f
    # yields the initial guess:
    N_guess = 1070379110485
    ans = arranged_probability(N_guess)
    print(
        "First arrangement containing over 1e12 discs & satisfying p(BB) = 1/2:\n"
        + f"N = {ans[0]}, b = {ans[1]}"
    )
