# from itertools import permutations

# # for comb in product(range(4), repeat = 11):
# #     print(comb)

# T = int(input())

# for test_case in range(1, T + 1):
#     N = int(input())
#     op_n = list(map(int, input().split()))
#     nums = list(map(int, input().split()))

#     # 사용되는 연산자들
#     ops = []
#     for i in range(4):
#         for k in range(op_n[i]):
#             ops.append(i)

#     result_min = 100000000
#     result_max = -100000000
    
#     for perm in permutations(ops, N-1):
#         result = nums[0]
#         for idx, op in enumerate(perm):
#             # 0 : +, 1 : -, 2 : *, 3 : //
#             if op == 0:
#                 result += nums[idx+1]
#             elif op == 1:
#                 result -= nums[idx+1]
#             elif op == 2:
#                 result *= nums[idx+1]
#             else:
#                 result /= nums[idx+1]
#                 result = int(result)

#         result_min = min(result, result_min)
#         result_max = max(result, result_max)

#     print(f"#{test_case} {result_max - result_min}")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # op_n: [+, -, *, /] 의 개수
    add, sub, mul, div = map(int, input().split())
    nums = list(map(int, input().split()))

    result_min = int(1e9)  # 1,000,000,000
    result_max = int(-1e9) # -1,000,000,000
    
    def dfs(idx, current, add, sub, mul, div):
        global result_min, result_max
        
        # 모든 숫자를 다 계산했을 때 최댓값, 최솟값 갱신
        if idx == N:
            result_min = min(result_min, current)
            result_max = max(result_max, current)
            return

        # 남은 연산자가 있다면 해당 연산을 수행하고 다음 숫자로 넘어감 (재귀 호출)
        if add > 0:
            dfs(idx + 1, current + nums[idx], add - 1, sub, mul, div)
        if sub > 0:
            dfs(idx + 1, current - nums[idx], add, sub - 1, mul, div)
        if mul > 0:
            dfs(idx + 1, current * nums[idx], add, sub, mul - 1, div)
        if div > 0:
            dfs(idx + 1, int(current / nums[idx]), add, sub, mul, div - 1)

    dfs(1, nums[0], add, sub, mul, div)

    print(f"#{test_case} {result_max - result_min}")