"""
Q: The square root of 2 can be written as an infinite continued fraction.

  sqrt(2) = 1 + 1/(2 + 1/(2 + 1/ (...)))
 
The infinite continued fraction can be written, sqrt(2) = [1; (2)], (2)
indicates that 2 repeats ad infinitum. In a similar way,
sqrt(12) = [4; (1, 3, 1, 8)].
 
It turns out that the sequence of partial values of continued fractions for
square roots provide the best rational approximations. Let us consider the
convergents for sqrt(2).

  1 + 1/2 = 3/2
  1 + 1/(2 + 1/2) = 7/5
  1 + 1/(2 + 1/(2 + 1/2)) = 17/12
  1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29

Hence the sequence of the first ten convergents for sqrt(2) are:

  1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the most important mathematical constant,
  
  e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...].

The first ten terms in the sequence of convergents for e are:

  2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1 + 4 + 5 + 7 = 17.
Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.
 
A: 272
"""


def euler_convergent_numerator(n):
    # e = [2; 1, 2, 1,  1,4,1,    1,6,1,    ..., 1,2k,1, ...]
    #   = [a; b0,b1,b2, b3,b4,b5, b6,b7,b8, ...,            ]
    # nth numerator is calculated as:
    #   num_n = num_{n-1}*b_{n-1} + num_{n-2}
    x, y, z = 8, 3, 2
    for i in range(n - 1):
        b = 2 * ((i + 6) // 3) if i % 3 == 2 else 1
        x, y, z = b * x + y, x, y

    # python can handle the big numbers
    print("b={}, x,y,z = (\n  {},\n  {},\n  {}\n)".format(b, x, y, z))
    return sum(int(d) for d in str(z))


if __name__ == "__main__":
    N = 100
    print(
        "Sum of digits in numerator of {}th convergent ".format(N)
        + "of the continued fraction for e: {}".format(
            euler_convergent_numerator(N)
        )
    )
