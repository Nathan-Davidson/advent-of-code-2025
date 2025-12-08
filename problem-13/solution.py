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

def solve(problem: list[list[str]]) -> int:
    op = problem[-1].strip()
    numbers = ['' for _ in problem[0]]
    for row in problem[:-1]:
        for i, c in enumerate(row):
            numbers[i] += c.strip()
    numbers = [int(num) for num in numbers]
    total = numbers[0]
    for num in numbers[1:]:
        if op == '*':
            total *= num
        else:
            total += num
    return total

if __name__ == '__main__':
    main()