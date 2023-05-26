from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    total_weight = 0
    time = 0
    while bridge or truck_weights:  # 브릿지에 트럭이 있거나, 대기트럭이 있는 동안
        time += 1
        if bridge:  # 다리에 트럭이 있으면
            if time - bridge[0][1] >= bridge_length:  # 총경과시간에서 첫번재 시간을 뺀게 다리 길이보다 크거나 같으면
                total_weight -= bridge.popleft()[0]  # 다리에서 내리기

        if truck_weights:  # 대기트럭이 있으면
            if total_weight + truck_weights[0] <= weight:  # 첫번째 놈이랑 대기중인 놈 첫번째 더한 무게가 다리 무게보다 작으면
                truck = truck_weights.pop(0)  # 대기에서 빼기
                bridge.append((truck, time))  # 다리에 올리기
                total_weight += truck  # 무게 추가
    return time