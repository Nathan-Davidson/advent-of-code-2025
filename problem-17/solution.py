#!/bin/python3

import fileinput

def main():
    points = []
    
    for line in fileinput.input():
        points.append([int(n) for n in line.strip().split(',')])
        
    best = 0
    for i, point in enumerate(points):
        for j in range(i + 1, len(points)):
            best = max(best, area(point, points[j]))
    
    print(best)

def area(p1: list[int], p2: list[int]) -> int:
    x1, x2 = max(p1[0], p2[0]), min(p1[0], p2[0])
    y1, y2 = max(p1[1], p2[1]), min(p1[1], p2[1])
    return (x1 - x2 + 1) * (y1 - y2 + 1)

if __name__ == '__main__':
    main()