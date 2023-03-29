import sys

n = int(sys.stdin.readline().strip())

numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()

m = int(sys.stdin.readline().strip())

compare = list(map(int, sys.stdin.readline().split()))

"""
def half_search(a, numbers):
    if len(numbers) == 1:
        if a == numbers[0]:
            return 1
        else:
            return 0
    if a == numbers[len(numbers) // 2]:
        return 1
    elif a > numbers[len(numbers) // 2]:
        return half_search(a, numbers[len(numbers)//2 + 1:len(numbers)+1])
    elif a < numbers[len(numbers) // 2]:
        return half_search(a, numbers[0 :len(numbers) // 2 -1])

print(half_search(3, compare))

"""
def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2

    if array[mid] == target:
        return 1

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid+1, end)

for i in compare:
    print(binary_search(numbers, i, 0, n-1))

#슬라이싱을 하면 결국 전체 원소를 다 복사하게 되어 의미가 없어짐