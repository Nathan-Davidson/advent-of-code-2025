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
        
        if distance >= 100:
            rotations = distance // 100
            distance -= rotations * 100
            nZeros += rotations
            
        if distance == 0:
            continue
            
        if direction == 'L':
            if distance > dial and dial != 0:
                nZeros += 1
            dial -= distance
        elif direction == 'R':
            dial += distance
            if dial > 100:
                nZeros += 1
        
        dial %= 100
        
        if dial == 0:
            nZeros += 1
    
    print(nZeros)
        
if __name__ == '__main__':
    main()