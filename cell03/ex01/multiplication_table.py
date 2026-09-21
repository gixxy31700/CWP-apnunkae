#!/usr/bin/env python3
num = int(input("Enter a number \n"))

for i in range(10):
    result = (i) * num
    print(f"{i} x {num} = {result}")
    i += 1
