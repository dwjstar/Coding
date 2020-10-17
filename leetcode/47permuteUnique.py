def permuteUnique(nums) :
    def dfs(k, sub):
        nonlocal visited
        if k == n:
            res.append(sub[:])
            return
        for i in range(n):
            if visited[i]==0:
                if i > 0 and nums[i] == nums[i - 1] and visited[i-1]==0:
                    continue
                num = nums[i]
                if visited[i] == 0:
                    visited[i] = 1
                    sub.append(num)
                    dfs(k + 1, sub)
                    sub.remove(num)
                    visited[i] = 0

    res = []
    sub = []
    n = len(nums)
    visited = [0 for _ in range(n)]
    nums.sort()
    dfs(0, sub)
    return res

if __name__=='__main__':
    nums=[2,2,1,1]
    res=permuteUnique(nums)
    print(res)