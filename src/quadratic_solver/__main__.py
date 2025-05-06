import argparse
from .quadratic import QuadraticEquation

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", type=float, required=True)
    parser.add_argument("-b", type=float, required=True)
    parser.add_argument("-c", type=float, required=True)
    args = parser.parse_args()

    eq = QuadraticEquation(args.a, args.b, args.c)
    result = eq.solve()

    if result is None:
        print("Pas de solutions réelles.")
    elif len(result) == 1:
        print(f"x = {result[0]}")
    else:
        print(f"x1 = {result[0]}")
        print(f"x2 = {result[1]}")

if __name__ == "__main__":
    main()
