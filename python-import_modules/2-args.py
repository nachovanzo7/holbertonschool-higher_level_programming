#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv) - 1))
        for x in range(1, len(sys.argv)):
            print("{}: {}".format((x), sys.argv[x]))
    elif len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print("1 argument:")
        print("{}: {}".format(1, sys.argv[1]))
