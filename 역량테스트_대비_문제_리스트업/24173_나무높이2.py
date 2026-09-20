# from collections import deque

# T = int(input())

# for test_case in range(1, T + 1):
#     N = int(input())
#     tree_heights = list(map(int, input().split()))
#     max_height = max(tree_heights)
#     day = 1

#     # 흠..일단 가장 높은 나무가 되려면 얼마나 키가 더 커야 하는지 구해놓은
#     # 행렬을 하나 만들어놔야 할 것 같다. 
#     to_grows = [max_height] * N
#     for i in range(N):
#         to_grows[i] -= tree_heights[i]

#     # [0, 0, ..., 0]까지 가는 최단경로? dfs?
#     q = deque([(to_grows, day)])
#     while q:
#         m_to_grows, day = q.popleft()
#         if sum(m_to_grows) == 0:
#             answer = day
#         # 3일 주기로 주는 물의 양 바뀌는거 
#         water = (day-1) % 3 + 1 # 1일차엔 1, 2일차엔 2, 3일차엔 3, 4일차엔 1
#         for i in range(N):
#             # 물을 줘도 아직 더 자랄 게 남아있다면 큐에 추가
#             if m_to_grows[i] - water >= 0:
#                 # 성장해야 할 수치 물만큼 빼주기
#                 no_water = m_to_grows[:]
#                 m_to_grows[i] -= water
#                 q.append((m_to_grows[:], day+1))
#                 # 원복
#                 m_to_grows[i] += water
#                 q.append(((m_to_grows[:], day+1)))

#     print(f"#{test_case} {answer}")

def check(D, diffs):
    # D일 동안 주어지는 1, 2, 3 물의 개수
    c1 = (D + 2) // 3
    c2 = (D + 1) // 3
    c3 = D // 3
    
    need_3 = 0
    need_2 = 0
    need_1 = 0
    tradeable_4s = 0  # (3+1) 대신 (2+2)로 바꿀 수 있는 기회
    tradeable_6s = 0  # (3+3) 대신 (2+2+2)로 바꿀 수 있는 기회
    
    for h in diffs:
        if h == 0: continue
        need_3 += h // 3
        rem = h % 3
        
        if rem == 2:
            need_2 += 1
        elif rem == 1:
            need_1 += 1
            if h >= 4:
                tradeable_4s += 1
        
        if h >= 6:
            tradeable_6s += (h // 3) // 2

    # [Step 1] 물 3이 부족한 경우: 3을 쪼개서 2와 1로 만듦
    if need_3 > c3:
        short_3 = need_3 - c3
        
        # 1. 1이 늘어나는 걸 방지하기 위해 (3, 3) -> (2, 2, 2) 우선 교환
        use_6 = min(tradeable_6s, (short_3 + 1) // 2)
        need_3 -= use_6 * 2
        need_2 += use_6 * 3
        short_3 = max(0, need_3 - c3)
        
        # 2. (3, 1) -> (2, 2) 교환 (오히려 1이 줄어듦)
        use_4 = min(tradeable_4s, short_3)
        need_3 -= use_4
        need_1 -= use_4
        need_2 += use_4 * 2
        tradeable_4s -= use_4
        short_3 = max(0, need_3 - c3)
        
        # 3. 그래도 부족하면 단순 분할 3 -> (2, 1)
        need_3 -= short_3
        need_2 += short_3
        need_1 += short_3

    # [Step 2] 물 1이 부족한 경우: (3, 1) 세트를 (2, 2)로 교환하여 1을 절약
    if need_1 > c1:
        short_1 = need_1 - c1
        use_4 = min(tradeable_4s, short_1, need_3)
        need_1 -= use_4
        need_3 -= use_4
        need_2 += use_4 * 2
        
    # [Step 3] 물 2가 부족한 경우: 2를 (1, 1)로 쪼갬
    if need_2 > c2:
        short_2 = need_2 - c2
        need_2 -= short_2
        need_1 += short_2 * 2

    # 최종적으로 필요한 물의 개수가 우리가 가진 물의 개수 이하면 성공!
    return need_3 <= c3 and need_2 <= c2 and need_1 <= c1


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    tree_heights = list(map(int, input().split()))
    max_height = max(tree_heights)
    
    diffs = [max_height - h for h in tree_heights if max_height - h > 0]
    
    if not diffs:
        print(f"#{test_case} 0")
        continue
        
    # 이분 탐색
    low = 1
    high = sum(diffs) * 3  # 충분히 큰 최대 날짜
    answer = high
    
    while low <= high:
        mid = (low + high) // 2
        if check(mid, diffs):
            answer = mid
            high = mid - 1  # 더 적은 날짜가 가능한지 탐색
        else:
            low = mid + 1
            
    print(f"#{test_case} {answer}")