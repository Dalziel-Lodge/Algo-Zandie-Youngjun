import sys

n, m = map(int, sys.stdin.readline().split())

pokemons = {}
questions = []

for i in range(n):
    name = sys.stdin.readline().strip()
    pokemons[name] = i+1

keys = list(pokemons.keys())
for _ in range(m):
    questions.append(sys.stdin.readline().strip())

for question in questions:
    try:
        idx = int(question)
        print(keys[idx-1])
    except ValueError:
        print(pokemons[question])