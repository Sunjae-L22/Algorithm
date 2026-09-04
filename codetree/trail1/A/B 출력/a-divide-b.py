a, b = map(int, input().split())
q = a * 10**20 // b          # 소수점 20자리까지 정수로 (//가 내림)
sign = '-' if q < 0 else ''
q = abs(q)
print(f"{sign}{q // 10**20}.{q % 10**20:020d}")