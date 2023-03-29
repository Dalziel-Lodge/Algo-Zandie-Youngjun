from collections import deque

# 테스트 케이스 수 입력 받기
t = int(input())

for _ in range(t):
    # 문서의 개수와 몇 번째로 인쇄되었는지 궁금한 문서의 위치 입력 받기
    n, m = map(int, input().split())

    # 문서의 중요도 입력 받기
    docs = list(map(int, input().split()))

    # Queue에 문서와 인덱스를 저장하기
    queue = deque([(i, doc) for i, doc in enumerate(docs)])

    # 출력 순서를 저장할 변수 초기화
    count = 0

    while queue:
        # Queue에서 가장 앞에 있는 문서를 꺼내기
        curr_doc = queue.popleft()

        # 현재 문서보다 중요도가 높은 문서가 있다면
        if any(curr_doc[1] < doc[1] for doc in queue):
            # 현재 문서를 Queue의 가장 뒤로 보내기
            queue.append(curr_doc)
        else:
            # 현재 문서를 출력하고 출력 순서를 1 증가시키기
            count += 1
            # 만약 출력하려는 문서라면 count 출력하고 반복문 종료
            if curr_doc[0] == m:
                print(count)
                break