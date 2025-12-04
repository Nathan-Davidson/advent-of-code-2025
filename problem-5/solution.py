#!/bin/python3

import fileinput

def main():
    totalJoltage = 0
    
    for bank in fileinput.input():
        totalJoltage += maxJoltage(bank.strip())
    
    print(totalJoltage)
        
def maxJoltage(bank: str) -> int:
    first = max(bank[:-1])
    second = max(bank[bank.index(first) + 1:])
    return int(first + second)
    
if __name__ == '__main__':
    main()