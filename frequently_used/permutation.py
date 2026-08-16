def permutation(arr, m):
    result, path, used = [], [], [False] * len(arr)

    def dfs(depth):
        if depth == m:
            result.append(path[:])
            return
        for i in range(len(arr)):
            if used[i] == True:
                continue
            used[i] = True
            path.append(arr[i])
            dfs(depth + 1)
            path.pop()
            used[i] = False

    dfs(0)
    return result


def combination(arr, m):
    result, path = [], []

    def dfs(start):
        if len(path) == m:
            result.append(path[:])
            return

        for i in range(start, len(arr)):
            path.append(arr[i])
            dfs(i+1)
            path.pop()

    dfs(0)
    return result


print(permutation(range(4), 3))
print("============================================================================")
print(combination(range(5), 3))