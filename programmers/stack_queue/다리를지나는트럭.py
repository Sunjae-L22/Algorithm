from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    now_weight = 0
    on_bridge = deque()

    # while True:
    #     answer += 1
    #     # 모든 트럭이 도착하면 끝
    #     if arrived == truck_n:
    #         break
    #     # 견딜수 있는 무게만큼 트럭 올라가기
    #     if now_weight < weight and truck_weights:
    #         truck = truck_weights.popleft()
    #         now_weight += truck
    #         on_bridge.append(0)
    #         # 초과되면 내리기
    #         if now_weight > weight:
    #             truck_weights.append(truck)
    #             now_weight -= truck
    #             on_bridge.pop()
    #     if on_bridge:
    #         for i in range(len(on_bridge)):
    #             on_bridge[i] += 1
    #             if on_bridge[i] == bridge_length:
    #                 on_bridge.pop()
    #                 arrived += 1
        
    # return answer
    while truck_weights or on_bridge:
        answer += 1
        for t in on_bridge:                  # 먼저 진행
            t[0] += 1
        while on_bridge and on_bridge[0][0] == bridge_length:
            now_weight -= on_bridge.popleft()[1]   # 무게 빼기!
        if truck_weights and now_weight + truck_weights[0] <= weight:
            t = truck_weights.popleft()
            now_weight += t
            on_bridge.append([0, t])
    return answer