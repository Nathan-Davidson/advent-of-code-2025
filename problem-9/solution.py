#!/bin/python3

import fileinput

def main():
    ranges = []
    queries = []
    
    for line in fileinput.input():
        if not line.strip():
            continue
        
        if '-' in line:
            lo, hi = line.split('-')
            ranges.append([int(lo), int(hi)])
        else:
            queries.append(int(line))
    
    fresh = 0
    for q in queries:
        for lo, hi in ranges:
            if lo <= q and q <= hi:
                fresh += 1
                break
    
    print(fresh)
    
if __name__ == '__main__':
    main()