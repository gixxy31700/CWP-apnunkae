#!/usr/bin/env python3
import math
num = float(input("Give me a number: \n"))
if math.ceil(num) - num == 0:
    print("This number is an integer.")
else:
    print("This number is a demical.") 