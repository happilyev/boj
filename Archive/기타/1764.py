import sys
n, m = map(int, sys.stdin.readline().split())
n_list = set([sys.stdin.readline().strip() for _ in range(n)])
m_list = set([sys.stdin.readline().strip() for _ in range(m)])
inter = n_list & m_list
print(len(inter))
for i in sorted(list(inter)): print(i)
