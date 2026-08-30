# 개선판: 매 턴 전체 후보표를 만들지 말고, "새 대상이 필요한 타워"만 자기 사정거리를 훑는다
from collections import deque

def init(N, mMap):
    global road, road_n, cover_cells, covering, towers, tower_n, occupant
    st = en = None
    for r in range(N):
        for c in range(N):
            if mMap[r][c] == 2: st = (r, c)
            elif mMap[r][c] == 3: en = (r, c)
    # 길은 갈래가 없으므로 앞으로 한 칸씩 따라가면 된다 (DFS 스택보다 짧고 가지에도 안 흔들린다)
    road = [st]
    prev, cur = None, st
    while cur != en:
        r, c = cur
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and (nr,nc) != prev and mMap[nr][nc] in (1,3):
                prev, cur = cur, (nr,nc)
                road.append(cur)
                break
        else:
            break
    road_n = len(road)
    idx_of = {cell: i for i, cell in enumerate(road)}
    cover_cells = []              # 타워 -> 사정거리 안의 road 인덱스 목록
    covering = [[] for _ in range(road_n)]
    towers = []
    tower_n = 0
    occupant = [-1] * road_n      # road 칸 -> 그 칸에 선 도망자 pid (없으면 -1)
    globals()['_idx_of'] = idx_of
    globals()['_N'] = N

def addTower(mRow, mCol, mInterval):
    global tower_n
    cells = []
    for dr in range(-3, 4):
        span = 3 - abs(dr)
        for dc in range(-span, span + 1):
            if dr == 0 and dc == 0: continue
            i = _idx_of.get((mRow + dr, mCol + dc))
            if i is not None:
                cells.append(i)
                covering[i].append(tower_n)
    cover_cells.append(cells)
    towers.append(mInterval)
    tower_n += 1

def runSimulation(M, mInterval, mHP, mRetTs, mRetHP):
    target = [-1] * tower_n
    ready  = [0]  * tower_n
    for i in range(road_n): occupant[i] = -1

    hp   = {}          # pid -> 남은 체력
    at   = {}          # pid -> road 인덱스
    gen, t = 0, 0

    while gen < M or at:
        t += 1
        # 새 대상이 필요한 타워만 골라서 자기 사정거리를 훑는다
        for i in range(tower_n):
            if t < ready[i]: continue
            tgt = target[i]
            if tgt != -1 and tgt in hp:
                # 직전 대상이 살아 있고 사정거리 안이면 그대로 유지
                if occupant[at[tgt]] == tgt and any(occupant[rc] == tgt for rc in cover_cells[i]):
                    continue
            best = -1; bh = 0
            for rc in cover_cells[i]:
                pid = occupant[rc]
                if pid == -1: continue
                if best == -1 or (hp[pid], pid) < (bh, best):
                    best = pid; bh = hp[pid]
            target[i] = best
        # 동시 공격
        for i in range(tower_n):
            if t < ready[i] or target[i] == -1: continue
            hp[target[i]] -= 1
            ready[i] = t + towers[i]
        # 사망
        for pid in [p for p, h in hp.items() if h <= 0]:
            mRetTs[pid] = t; mRetHP[pid] = 0
            occupant[at[pid]] = -1
            del hp[pid]; del at[pid]
        # 이동 / 등장 / 탈출
        if t % mInterval == 0:
            for pid in at: at[pid] += 1
            if gen < M:
                at[gen] = 0; hp[gen] = mHP; gen += 1
            for pid in [p for p, i in at.items() if i == road_n - 1]:
                mRetTs[pid] = t; mRetHP[pid] = hp[pid]
                del hp[pid]; del at[pid]
            for i in range(road_n): occupant[i] = -1
            for pid, i in at.items(): occupant[i] = pid
