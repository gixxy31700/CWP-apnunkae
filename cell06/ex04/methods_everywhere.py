#!/usr/bin/env python3
import sys

def shrink(string):
    print(string[:8])

def enlarge(string):
    print(string + 'Z' * (8 - len(string)))

if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)