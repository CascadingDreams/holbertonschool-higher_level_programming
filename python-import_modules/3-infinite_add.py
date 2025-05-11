#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_num = len(sys.argv) - 1
    sum = 0

    for i in range(arg_num):
        arg = int(sys.argv[i + 1])
        sum += arg
    print("{}".format(sum))
