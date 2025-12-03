#!/bin/python3

import re
import sys

def main():
    invalidSum = 0
    rawInput = sys.stdin.readline()
    ranges = rawInput.split(',')
    for r in ranges:
        invalidSum += processRange(r)
    print(invalidSum)
    
def processRange(r: str) -> int:
    res = 0
    lo, hi = r.split('-')
    for i in range(int(lo), int(hi) + 1):
        if not validate(i):
            res += i
    return res
    
def validate(n: int) -> bool:
    num = str(n)
    for f in factors(len(num)):
        if not checkPartition(num, f):
            return False
    return True

def checkPartition(n: str, l: int) -> bool:
    parts = set()
    for start in range(0, len(n), l):
        parts.add(n[start:start + l])
    return len(parts) != 1

# input range is probably small enough it's easier to just hardcode this
factorsCache = {}
def factors(n: int) -> list[int]:
    if n not in factorsCache:
        res = set()
        i = 1
        while i ** 2 <= n:
            if n % i == 0:
                res.add(i)
                res.add(n // i)
            i += 1
        res.remove(n) # trim this because when you're using these you don't want to split into 1 group
        factorsCache[n] = list(res)
    return factorsCache[n]

if __name__ == '__main__':
    main()