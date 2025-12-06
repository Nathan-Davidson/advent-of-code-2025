#!/bin/python3

import fileinput

def main():
    ranges = []
    
    for line in fileinput.input():
        if not line.strip():
            continue
        
        if '-' in line:
            lo, hi = line.split('-')
            ranges.append([int(lo), int(hi)])
    
    ranges = sorted(ranges)
    merged = []
    curr = ranges.pop(0)
    while ranges:
        if ranges[0][0] <= curr[1]:
            curr[1] = max(curr[1], ranges[0][1])
            ranges.pop(0)
        else:
            merged.append(curr)
            curr = ranges.pop(0)
    merged.append(curr)
    
    fresh = 0
    for lo, hi in merged:
        fresh += hi
        fresh -= lo
        fresh += 1
    
    print(fresh)
    
if __name__ == '__main__':
    main()