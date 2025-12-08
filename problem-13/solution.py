#!/bin/python3

import fileinput

def main():
    diagram = []
    
    for line in fileinput.input():
        diagram.append([c for c in line[:-1].replace('S', '|')])
    
    splits = set()
    for r in range(1, len(diagram)):
        for c, ch in enumerate(diagram[r]):
            if diagram[r - 1][c] != '|':
                continue
            
            if ch == '.':
                diagram[r][c] = '|'
            elif ch == '^':
                splits.add((r,c))
                if c - 1 >= 0 and diagram[r][c - 1] == '.':
                    diagram[r][c - 1] = '|'
                if c + 1 < len(diagram[r]) and diagram[r][c + 1] == '.':
                    diagram[r][c + 1] = '|'
    
    print(len(splits))
    
if __name__ == '__main__':
    main()