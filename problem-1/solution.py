#!/bin/python3

import fileinput
import re
import sys

def main():
    dial = 50
    nZeros = 0
    
    for line in fileinput.input():
        match = re.match(r'([LR])(\d+)', line)
        if not match:
            print('malformed input')
            sys.exit(1)
        
        direction = match.group(1)
        distance = int(match.group(2))
            
        if direction == 'L':
            dial -= distance
        elif direction == 'R':
            dial += distance
        
        if dial < 0 or dial >= 100:
            dial %= 100
        
        if dial == 0:
            nZeros += 1
        
    print(nZeros)
        
if __name__ == '__main__':
    main()