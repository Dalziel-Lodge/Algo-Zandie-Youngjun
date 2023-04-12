import sys
import heapq

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    max_heap = []    # 최대힙을 저장할 리스트
    min_heap = []    # 최소힙을 저장할 리스트
    visited = [False] * 1000001  # value 범위: -1000000 <= value <= 1000000

    # 명령어를 입력받아 처리하는 반복문
    for i in range(n):
        op, num = sys.stdin.readline().split()
        num = int(num)

        # "I" 명령어 처리
        if op == 'I':
            heapq.heappush(min_heap, (num, i))     # 최소힙에 (num, i)를 추가
            heapq.heappush(max_heap, (-num, i))    # 최대힙에 (-num, i)를 추가
            visited[i] = True                      # visited 리스트의 i번째 인덱스를 True로 변경

        # "D" 명령어 처리
        elif op == 'D':
            # "D 1" 처리
            if num == 1:
                # 최대힙에서 visited가 False인 인덱스를 모두 제거
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)

                # 최대힙이 비어있지 않으면 visited를 False로 변경하고 최대힙에서 pop
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            # "D -1" 처리
            else:
                # 최소힙에서 visited가 False인 인덱스를 모두 제거
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                # 최소힙이 비어있지 않으면 visited를 False로 변경하고 최소힙에서 pop
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    # visited가 False인 인덱스를 모두 제거
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    # 최대힙과 최소힙이 모두 비어있으면 "EMPTY" 출력
    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
