l = int(input())
chars = list(input())

result = 0
m = 1234567891
r = 31

sum_char = 0
for i in range(len(chars)):
    sum_char += (ord(chars[i])-ord('a') + 1)*(r**i)

result = sum_char % m
print(result)