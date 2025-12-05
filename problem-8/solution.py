#!/bin/python3

import fileinput

def main():
    puzzle = []
    
    for line in fileinput.input():
        puzzle.append([c for c in line.strip()])
    
    reachable = 0
    while True:
        r = removeReachable(puzzle)
        if r == 0:
            break
        reachable += r
                
    print(reachable)

def removeReachable(puzzle: list[list[str]]) -> int:
    reachable = 0
    for r in range(len(puzzle)):
        for c in range(len(puzzle[r])):
            if isReachable(puzzle, r, c):
                reachable += 1
    
    for r in range(len(puzzle)):
        for c in range(len(puzzle[r])):
            if puzzle[r][c] == 'X':
                puzzle[r][c] = '.'
    
    return reachable

def isReachable(puzzle: list[list[str]], row: int, col: int) -> bool:
    if lookup(puzzle, row, col) != '@':
        return False
    
    neighbors = [
        lookup(puzzle, row - 1, col - 1),
        lookup(puzzle, row - 1, col),
        lookup(puzzle, row - 1, col + 1),
        lookup(puzzle, row, col - 1),
        lookup(puzzle, row, col + 1),
        lookup(puzzle, row + 1, col - 1),
        lookup(puzzle, row + 1, col),
        lookup(puzzle, row + 1, col + 1),
    ]
    
    reachable = len([n for n in neighbors if n != '.']) < 4
    if reachable:
        puzzle[row][col] = 'X'
    return reachable

def lookup(puzzle: list[list[str]], row: int, col: int) -> str:
    if row < 0 or row >= len(puzzle) or col < 0 or col >= len(puzzle[row]):
        return '.' # out of bounds spaces are free
    return puzzle[row][col]
    
if __name__ == '__main__':
    main()