import math

a, b, v = map(int, input().split())
day = 0
height = (v-b)/(a-b)

print(math.ceil(height))