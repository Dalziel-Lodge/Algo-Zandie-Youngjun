import sys

m = int(sys.stdin.readline().strip())
a = set()

command = []

def check(a: set, b: int):
    if b in a:
        print(1)
    else:
        print(0)


def toggle(a: set, b: int):
    if b in a:
        a.remove(b)
    else:
        a.add(b)

def all(a: set):
    a.clear()
    a.update(range(1, 21))

def empty(a: set):
    a.clear()

for _ in range(m):
    command = sys.stdin.readline().split()
    if command[0] == "add":
        a.add(int(command[1]))
    elif command[0] == "remove":
        try:
            a.remove(int(command[1]))
        except:
            pass
    elif command[0] == "check":
        check(a, int(command[1]))
    elif command[0] == "toggle":
        toggle(a, int(command[1]))
    elif command[0] == "all":
        all(a)
    elif command[0] == "empty":
        empty(a)