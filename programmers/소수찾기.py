def permutation(arr, m):
    result, path, used = [], [], [False] * len(arr)

    def dfs(depth):
        if depth == m:
            result.append(path[:])
            return
        for i in range(len(arr)):
            if used[i]:
                continue
            used[i] = True
            path.append(arr[i])
            dfs(depth + 1)
            path.pop()
            used[i] = False

    dfs(0)
    return result



def is_it_prime(num):
    prime = True

    # 2는 무조건 소수
    if num == 2:
        return True

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            prime = False
            break

    return prime




numbers = input()
answer = 0
    
# 문자열 numbers를 정수 배열로 변환
int_numbers = []
for number in numbers:
    int_numbers.append(int(number))

perm_list = []
# 길이 1부터 배열 길이까지의 순열조합 모두 확인
for i in range(1, len(int_numbers)+1):
    perm_list.append(permutation(int_numbers, i))
    
num = 0
print(perm_list)
for perms in perm_list:
    for perm in perms:
    # 뒤에서부터 차례대로 1, 10, 100곱해서 숫자 만들기
        for i in range(len(perm)):
            num += int(perm[len(perm) - i - 1]) * 10 ** i
        
if is_it_prime(num):
    answer += 1