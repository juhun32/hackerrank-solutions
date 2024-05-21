import sys
from itertools import permutations
input = sys.stdin.readline

inp, num = input().strip().split()
pmt = list(permutations(inp, int(num)))
temp = sorted(i for i in pmt)

for i in temp:
    print(*i, sep='')