#n시 OO분 OO초
#3시, 13시, 23시
#3분, 13분, 23분, 30분, 31분, 32분, 33분, 34분, 35분, 36분, 37분, 38분, 39분, 43분, 53분
#3초, 13초, 23초, 30초, 31초, 32초, 33초, 34초, 35초, 36초, 37초, 38초, 39초, 43초, 53초

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            time = str(i) + ":" + str(j) + ":" + str(k)
            print(time)
            if '3' in time:
                count += 1

print(count)