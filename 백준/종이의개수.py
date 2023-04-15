import sys

n = int(sys.stdin.readline().strip())
papers = []

for _ in range(n):
    papers.append(list(map(int, sys.stdin.readline().split())))

count_0, count_1, count_minus1 = 0, 0, 0

def check_paper(x, y, scope):
    num = papers[x][y]
    global count_0, count_1, count_minus1
    #여기 주의
    #영역만틈 탐색해야함
    for i in range(x, x + scope):
        for j in range(y, y + scope):
            if papers[i][j] != num:
                check_paper(x, y, scope // 3)
                check_paper(x + scope // 3, y, scope // 3)
                check_paper(x + (2 * (scope // 3)), y, scope // 3)
                check_paper(x, y + scope // 3, scope // 3)
                check_paper(x + scope // 3, y + scope // 3, scope // 3)
                check_paper(x + (2 * (scope // 3)), y + scope // 3, scope // 3)
                check_paper(x, y + (2 * (scope // 3)), scope // 3)
                check_paper(x + scope // 3, y + (2 * (scope // 3)), scope // 3)
                check_paper(x + (2 * (scope // 3)), y + (2 * (scope // 3)), scope // 3)
                return
    if num == 0:
        count_0 += 1
    elif num == 1:
        count_1 += 1
    elif num == -1:
        count_minus1 += 1


check_paper(0, 0, n)
print(count_minus1)
print(count_0)
print(count_1)