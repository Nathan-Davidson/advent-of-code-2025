#!/bin/python3

import fileinput

def main():
    diagram = []
    
    for line in fileinput.input():
        diagram.append([c for c in line[:-1]])
    reaches = [0 for _ in diagram[0]]
    
    for i, c in enumerate(diagram[0]):
        if c == 'S':
            reaches[i] = 1
            diagram[0][i] = '|'
    
    for r in range(1, len(diagram)):
        for c, ch in enumerate(diagram[r]):
            if diagram[r - 1][c] != '|':
                continue
            
            if ch == '.':
                diagram[r][c] = '|'
            elif ch == '^':
                paths = reaches[c]
                reaches[c] = 0
                if c - 1 >= 0 and diagram[r][c - 1] != '^':
                    diagram[r][c - 1] = '|'
                    reaches[c - 1] += paths
                if c + 1 < len(diagram[r]) and diagram[r][c + 1] != '^':
                    diagram[r][c + 1] = '|'
                    reaches[c + 1] += paths
    
    print(sum(reaches))

if __name__ == '__main__':
    main()