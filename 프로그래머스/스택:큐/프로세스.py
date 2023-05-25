from collections import deque


def solution(priorities, location):
    queue = deque(enumerate(priorities))
    count = 0
    answer = 0

    while queue:
        flag = 0  # any를 사용하면 flag를 사용하지 않고 더 효율적으로 코드작성 가능
        element = queue.popleft()

        for i in list(queue):
            if i[1] > element[1]:
                queue.append(element)
                break
            flag += 1

        if flag == len(list(queue)):
            count += 1
            if element[0] == location:
                answer = count
                return answer

    return answer