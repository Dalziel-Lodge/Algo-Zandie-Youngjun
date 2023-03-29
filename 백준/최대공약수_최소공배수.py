import sys

a, b = map(int, sys.stdin.readline().split())

def gcm(a, b): #최소 공배수
    for i in range(max(a,b), a*b+1):
        if i % a == 0 and i % b == 0:
            return i



def lcd(a, b): #최대공약수
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

print(lcd(a,b))
print(a*b//lcd(a,b))
#두수의 곱을 최대공약수로 나누면 최소공배수가 된다.
