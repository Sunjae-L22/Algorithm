# 2559 수열 [실버 3]

# N : 전체 날짜 수, K : 합을 구하기 위한 연속적인 날짜의 수
N, K = map(int, input().split())
temparatures = list(map(int, input().split()))

# 누적합을 만들어놓고 게산
cum_sum = [0] * N
cum_sum[0] = temparatures[0]
for i in range(1, N):
    cum_sum[i] = cum_sum[i-1] + temparatures[i]

# N일에서 K일씩 연속되게 한 합의 개수 : N - K + 1
k_sum = [0] * (N-K+1)
k_sum[0] = cum_sum[K-1]
for i in range(1, N-K+1):
    k_sum[i] = cum_sum[i+K-1] - cum_sum[i-1]

print(max(k_sum))