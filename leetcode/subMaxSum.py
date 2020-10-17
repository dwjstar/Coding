def maxSubArray(nums) -> int:
    if not nums:
        return
    len_nums = len(nums)
    if len_nums < 2:
        return nums[0]
    dp = [0] * len_nums
    dp[0] = nums[0]
    for i in range(1, len_nums):
        dp[i] = max(dp[i] + dp[i - 1], nums[i])
    print(dp)
    return max(dp)

if __name__=='__main__':
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))