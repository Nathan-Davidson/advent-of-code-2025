#!/bin/python3

import fileinput
import re

def main():
    problems = []
    
    for line in fileinput.input():
        problems.append(re.split(r'\s+', line.strip()))
    
    total = 0
    for c in range(len(problems[0])):
        t = int(problems[0][c])
        op = problems[-1][c]
        for r in range(1, len(problems) - 1):
            if op == '*':
                t *= int(problems[r][c])
            elif op == '+':
                t += int(problems[r][c])
        total += t
    
    print(total)
    
if __name__ == '__main__':
    main()