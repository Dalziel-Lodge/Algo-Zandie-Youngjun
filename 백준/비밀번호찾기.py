import sys

n, m = map(int, sys.stdin.readline().split())

my_dict = {}

for _ in range(n):
    url, password = map(str, sys.stdin.readline().split())
    my_dict[url] = password

for _ in range(m):
    problem = sys.stdin.readline().strip()
    print(my_dict[problem])