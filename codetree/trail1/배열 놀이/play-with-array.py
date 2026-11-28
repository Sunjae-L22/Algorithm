N, Q = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(Q):
    querys = list(map(int, input().split()))
    if querys[0] == 1:
        print(nums[querys[1]-1])
    elif querys[0] == 2:
        if querys[1] in nums:
            print(nums.index(querys[1])+1)
        else:
            print(0)
    else:
        for i in range(querys[1]-1, querys[2]):
            print(nums[i], end = ' ')
        print()