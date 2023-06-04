"""
Q: It turns out that 12 cm is the smallest length of wire that can be bent to
form an integer sided right angle triangle in exactly one way, but there are
many more examples.

  12 cm: (3, 4, 5)
  24 cm: (6, 8, 10)
  30 cm: (5, 12, 13)
  36 cm: (9, 12, 15)
  40 cm: (8, 15, 17)
  48 cm: (12, 16, 20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer
sided right angle triangle, and other lengths allow more than one solution to be
found; for example, using 120 cm it is possible to form exactly three different
integer sided right angle triangles.

  120 cm: (30, 40, 50), (20, 48, 52), (24, 45, 51)

Given that L is the length of the wire, for how many values of L <= 1500000 can
exactly one integer sided right angle triangle be formed?

A: 
"""


def singular_integer_right_triangles(l):

    singular_solns = 0
    for perimeter in range(l+1):
        print(f"Checking perimeter = {perimeter}")
        n_sols = 0
        for c in range(1, perimeter//2):
            if n_sols > 1:
                    break
                
            for x in range(c+1, (c + perimeter)//2 + 1):
                if n_sols > 1:
                    break
                
                # a + b + c = perimeter
                a, b = x - c, perimeter - x
                #print(f"  perimeter = {perimeter}, a={a} b={b} c={c}")
                n_sols += (a**2 + b**2 == c**2)

        if n_sols == 1:
            print(f"  Singular solution found!")
            
        singular_solns += (n_sols == 1)
            
    return singular_solns


if __name__ == "__main__":
    L = 1500000
    print(
        f"Answer: {singular_integer_right_triangles(L)}"
    )
