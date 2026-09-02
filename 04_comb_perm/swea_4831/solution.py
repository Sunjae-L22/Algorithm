import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charger = set(map(int, input().split()))

    cur, cnt, ok = 0, 0, True

    # 한 번에 종점까지 못 가면
    while cur + K < N:                     
        nxt = -1
        # 사정거리 안에서 먼 쪽부터
        for p in range(cur + K, cur, -1):   
            if p in charger:
                nxt = p
                break
        # 갈 수 있는 충전소가 없다 -> 종료
        if nxt == -1:                       
            ok = False
            break
        cur, cnt = nxt, cnt + 1

    print(f"#{tc} {cnt if ok else 0}")