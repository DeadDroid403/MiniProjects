#! /usr/bin/python3

import argparse
import sys
import hashlib

parser = argparse.ArgumentParser(description="tool for encoding into md5 hash",usage="%(prog)s -e cipher")

parser.add_argument("-e"
                    ,help="creats encoded md5 hash"
                    ,dest="code"
                    ,nargs="+"
                    ,metavar="encode"
                    ,type=str)

args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

code = args.code

if code:
    for i in code:
        print(hashlib.md5(i.encode()).hexdigest())