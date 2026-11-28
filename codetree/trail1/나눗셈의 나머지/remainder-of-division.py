A, B = map(int, input().split())
remainders = [0] * B

while A > 1:
    remainders[A % B] += 1
    A = A // B
    
ans = 0
for n in remainders:
    ans += n * n

print(ans)