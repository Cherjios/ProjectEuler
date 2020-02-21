#!/usr/bin/python3
""" Find the sum of all the multiples of 3 or 5 below 1000"""

res = 0
i = 0
j = 1000

while i < j:
    if (i % 3 == 0 or i % 5 == 0):
        res += i
    i += 1

print("Find the sum of all the multiples of 3 or 5 below 1000")
print("resut is {}".format(res))
