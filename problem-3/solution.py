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
    if len(num) % 2 != 0:
        return True
    if num[:len(num)//2] != num[len(num)//2:]:
        return True
    return False

if __name__ == '__main__':
    main()