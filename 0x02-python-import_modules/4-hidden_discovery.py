#!/usr/bin/python3
import hidden_4
def main():
    L = dir(hidden_4)
    for i in range(len(L)):
        if(L[i][0] != '_'):
            print("{}".format(L[i]))
if __name__ == "__main__":
    main()
