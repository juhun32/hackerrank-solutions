# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

d = defaultdict(list)

# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print(i)

n, m = map(int, input().split())

for i in range(n):
    d[input()].append(i + 1)

for j in range(m):
    ans = input()
    if ans in d:
        print(*d[ans])
    else:
        print(-1)
