#!/usr/bin/python3
import sys
def main(*argv):
    L = len(sys.argv)
    sum = 0
    if L > 1:
        for args in sys.argv:
            if args != sys.argv[0]:
                sum = sum + int(args)
    print(sum)
if __name__ == "__main__":
    main()
