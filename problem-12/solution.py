#!/bin/python3

import fileinput
import re

def main():
    raw = []
    
    for line in fileinput.input():
        raw.append(line[:-1])

    indexes = [i for i, c in enumerate(raw[-1]) if c in '*+']
    
    problems = []
    for i, lo in enumerate(indexes):
        problem = []
        
        for row in raw:
            hi = len(row)
            if i + 1 < len(indexes):
                hi = indexes[i + 1] - 1
            problem.append(row[lo:hi])
        problems.append(problem)
    
    total = 0
    for problem in problems:
        total += solve(problem)
    
    print(total)

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