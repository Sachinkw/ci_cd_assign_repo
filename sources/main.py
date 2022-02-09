from calculator import add, substract, multiply
import argparse
import sys


def calc(args):
    try:
        if args.o == 'add':
            return add(args.x, args.y)
        elif args.o == 'substract':
            return substract(args.x, args.y)
        elif args.o == 'multiply':
            return multiply(args.x, args.y)
        else:
            return "Enter valid operation!!"
    except Exception as e:
        return e
            
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', help="Enter first number")
    parser.add_argument('--y', help="Enter second number")
    parser.add_argument('--o', type=str, help="Which operation you want to perform? [add] [substract] [multiply]")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))