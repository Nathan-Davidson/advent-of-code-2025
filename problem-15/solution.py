#!/bin/python3

import fileinput
import heapq
import operator

from collections import defaultdict
from functools import reduce

def main():
    boxes = []
    
    for line in fileinput.input():
        boxes.append(tuple(int(n) for n in line.strip().split(',')))
    
    uf = UnionFind(len(boxes))
    
    distances = []
    for i, box in enumerate(boxes):
        for j in range(i + 1, len(boxes)):
            distances.append((distance(box, boxes[j]), i, j))
    heapq.heapify(distances)
    
    connections = 0
    while connections < 1000:
        d, i, j = heapq.heappop(distances)
        connections += 1
        uf.union(i, j)
    
    hist = defaultdict(int)
    for i in range(len(boxes)):
        hist[uf.find(i)] += 1
    sizes = sorted(hist.values())
    
    print(reduce(operator.mul, sizes[-3:], 1))

def distance(p1: tuple[int], p2: tuple[int]) -> int:
    d = 0
    for c1, c2 in zip(p1, p2):
        d += (c1 - c2) ** 2
    return d # I'm pretty sure taking the square root doesn't change the ordering so who cares

class UnionFind:
    def __init__(self, size: int):
        self.arr = list(range(size))
        
    def union(self, first: int, second: int) -> None:
        self.arr[self.find(first)] = self.find(second)
    
    def find(self, elem: int) -> int:
        if self.arr[elem] != elem:
            self.arr[elem] = self.find(self.arr[elem])
        return self.arr[elem]

if __name__ == '__main__':
    main()