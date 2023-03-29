import sys
while True:
    num = []
    tmp = sys.stdin.readline().strip()
    for i in tmp:
        num.append(int(i))
    if num == [0]:
        break
    if num == num[::-1]:
        print("yes")
    else:
        print("no")

