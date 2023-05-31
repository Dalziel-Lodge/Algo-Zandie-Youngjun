n = int(input())

num_range = 0
level = 0
loc = 0

for i in range(1, 10000000):
    if num_range >= n:
        loc = n - (num_range-(i-1))
        break
    else:
        num_range += i
        level += 1


if level % 2 == 0:
    print(loc, '/', level + 1 - loc, sep="")
else:
    print(level + 1 - loc, '/',loc , sep="")


'''
다른 사람의 풀이
n=int(input())
line=1

while n>line:
    n -= line
    line +=1
    
if line%2==0:
    print(n,'/',line-n+1,sep='')
else:
    print(line-n+1,'/',n,sep='')
'''

