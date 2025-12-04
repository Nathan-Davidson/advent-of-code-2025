#!/bin/python3

import fileinput

def main():
    totalJoltage = 0
    
    for bank in fileinput.input():
        totalJoltage += maxJoltage([c for c in bank.strip()])
    
    print(totalJoltage)
        
def maxJoltage(bank: str) -> int:
    res = []
    while bank:
        while len(res) and res[-1] < bank[0] and len(res) + len(bank) > 12:
            res.pop()
        n = bank.pop(0)
        if len(res) < 12:
            res.append(n)
    return int(''.join(res))
    
if __name__ == '__main__':
    main()