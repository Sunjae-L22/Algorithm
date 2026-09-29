'''
제한 조건
실행시간 : 50개의 테스트 케이스를 합쳐서 C/C++/JAVA의 경우 3초, 파이썬 10초
메 모 리 : Heap, Global, Stack 등을 모두 합해 최대 256MB까지 사용 가능 (단, 스택은 최대 1MB까지 사용 가능)

제출 횟수 제한
무제한

채점
답안을 제출하면 결과를 판정해서 실시간으로 알려주며 그 의미는 다음과 같다.
Accpet : Sample input에 대해 제출 완료
Fail : 오답 또는 부분점수 획득

평가
sample_input은 편의를 위해 제공하며, 실제 채점은 별도의 평가용 input으로 이루어진다.
제한 시간 이내에 평가용 input의 모든 테스트 케이스에 대해 정답을 도출하면 Pass 이며,
그 외에 오답, 부분 정답, 시간 제한을 초과하는 경우 1회 Fail이 된다.

마을 사무소에서는 마을의 공해를 줄이기 위해 주민들에게 한 집당 한 대씩 전기자동차를 보급하고, 전기자동차 충전소를 만들려고 한다.

마을에는 N개의 집이 있으며 ( 2 ≤ N ≤ 20 ),
마을의 전체 좌표는 아래 [ 그림 1 ]과 같이 X축과 Y축 방향 모두 -15 에서 15 까지이다.
이 안에, 각각 집의 위치는 ( x , y )로 주어진다. ( -15 ≤ x, y ≤ 15 )


마을 주민들은 집으로부터 일정 거리 이내에 충전소가 있을 경우에만 전기 자동차를 사용한다고 한다.
그래서 마을 사무소에선 주민들의 집과 충전소 간 거리를 감안하여, 충전소 위치를 정하여 만들려고 한다.

집과 충전소 간 거리를 구하는 방식은 다음과 같다.
예를 들어, 집의 위치가 (XH, YH) 이고 충전소의 위치가 (XC, YC) 이면, 집과 충전소 간 거리는
|XH – XC| + |YH – YC| 가 된다.

마을 내 모든 집에 전기 자동차가 보급될 수 있도록 충전소의 위치를 선정할 때,
▶ 충전소와 N개의 집 사이 거리의 합이 최소가 되는 값을 출력하는 프로그램을 작성하라.

단!
①  충전소는 최소한의 개수만 지어야 하며, 최대 2개까지 지을 수 있다.
     만약 충전소를 1개만 지어도, 마을 내 모든 집에 전기 자동차를 보급할 수 있다면, 충전소는 반드시 1개만 지어야 한다.

②  충전소를 2개 지을 경우, 각 집과 충전소간 거리는 가까운 충전소를 기준으로 한다.
     예를 들어 아래 [그림 2]와 같이 2 개의 집과 2 개의 충전소가 존재할 경우,
      A집과 충전소간 거리는 3 이 되고, B집과 충전소간 거리는 4 가 된다.

③ 만약 충전소를 2 개 지어도, 전기 자동차를 구입할 수 없는 집이 있을 경우에는, -1 를 출력한다.

④ 집이 있는 위치에는 충전소를 지을 수 없다.

아래의 [ 그림 3-1 ] 과 같이 A집( -2, 0 )과 B집( 1, 3 )이 있다고 가정하자.
A집에서 충전소까지 허용 가능한 최대 거리는 1 이고, B집에서 충전소까지 허용 가능한 최대 거리는 2 이다.

이와 같은 경우는 [ 그림 3-2 ]와 같이, 반드시 2개의 충전소가 필요하며, 이 때 충전소와 각 집 사이의 거리 합의 최소값은 2가 된다.

아래 [ 그림 4 ] 는 또 다른 예이다.
A집의 위치는 ( -1, -1 ) 이며 충전소까지 허용 가능한 최대 거리는 1 이고, B집의 위치는 ( 1, 0 )이며 충전소까지 허용 가능한 최대 거리는 2 이다.
이 경우 1 개의 충전소 건설( 붉은 색 원표시 부분 ) 만으로 충분하므로, 정답은 3 이 된다.

아래 [ 그림 5 ]와 같은 경우, 2개의 충전소 건설로도, 전기 자동차를 보급 할 수 없는 집이 생길 경우는 -1이 정답이 된다.

[제약 사항]
1. 집의 개수 N은,  2 ≤ N ≤ 20 범위의 정수이다.
2. 집의 좌표 (x, y)는, -15 ≤ x, y ≤ 15 범위의 정수이다.
3. 각 집에서 충전소까지의 허용 가능한 거리 d는, 1 ≤ d ≤ 30 범위의 정수이다.


[입력]
첫 줄에는 테스트 케이스의 개수 T가 주어진다.
그 다음 줄부터 각 테스트 케이스가 주어지며, 각 테스트 케이스의 첫째 줄에는 N이 오고,
다음 N줄에는 집의 위치 x, y 그리고 각 집에서 충전소까지 허용 가능한 거리 d가 한 칸씩 공백을 두고 주어진다.


[출력]
테스트 케이스의 결과는 "#C"를 찍고 한 칸 띄고 정답을 출력한다.
(단, C는 테스트 케이스의 번호를 의미하며 1 부터 시작한다.)

[출력 예]
#1 2
#2 3
#3 36
#4 -1
#5 21

'''

import sys
sys.stdin = open('sample_input1.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # (x, y, 최대거리)
    houses = [tuple(map(int, input().split())) for _ in range(N)]

    occupied = {(x, y) for x, y, _ in houses} # 집 좌표 집합 -> 충전소 지을수없음
    all_houses = set(range(N))
    candidates = []
    best_one = float('inf')

    # 충전소를 지을 수 있는 위치 탐색
    for x in range(-15, 16):
        for y in range(-15, 16):
            # 집이 있는 좌표면 건너뜀
            if (x, y) in occupied:
                continue

            # 지금 보고 있는 좌표에 지었을 때 이 충전소를 이용할 수 있는 집 번호
            covered = set()
            distances = []

            for i, (hx, hy, limit) in enumerate(houses):
                distance = abs(x - hx) + abs(y - hy)
                distances.append(distance)

                if distance <= limit:
                    covered.add(i)

            # 아무 집도 이용 못하는 위치 : 후보에서 제외
            if not covered:
                continue

            # 모든 집이 이용할 수 있으면 충전소 1개짜리 정답의 후보가 됨!!
            if len(covered) == N:
                best_one = min(best_one, sum(distances))

            candidates.append((covered, distances))

    # 1개로 가능하면 반드시 1개만 설치
    if best_one != float('inf'):
        print(f"#{tc} {best_one}")
        continue

    # 보통 커버하는 집이 많으면 좋은 답일 확률 높아지니까 정렬해줌
    candidates.sort(key=lambda item: len(item[0]), reverse=True)

    # 각 집에 닿을 수 있는 충전소 후보 번호
    by_house = [[] for _ in range(N)]
    for station_idx, (covered, _) in enumerate(candidates):
        for house_idx in covered:
            by_house[house_idx].append(station_idx)

    if any(not positions for positions in by_house):
        print(f"#{tc} -1")
        continue

    best_two = float('inf')

    for i, (covered_a, distances_a) in enumerate(candidates):
        missing = all_houses - covered_a

        # A가 닿지 못하는 집 중, 가능한 충전소 위치가 가장 적은 집
        pivot = min(missing, key=lambda h: len(by_house[h]))

        for j in by_house[pivot]:
            if j <= i:
                continue

            covered_b, distances_b = candidates[j]

            if not missing.issubset(covered_b):
                continue

            total = 0
            for da, db in zip(distances_a, distances_b):
                total += da if da < db else db

                if total >= best_two:
                    break

            if total < best_two:
                best_two = total

    answer = -1 if best_two == float('inf') else best_two
    print(f"#{tc} {answer}")