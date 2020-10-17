def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    if not candidates:  # 先解决空输入的情况
        return []

    candidates.sort()  # 排序
    res = []

    def backtrack(i, temp_sum, temp_list):
        """
        i：遍历到candidates数组中第几个元素
        temp_sum：目前遍历数组的和
        temp_list：目前遍历的数组
        """
        if temp_sum == target:
            res.append(temp_list)
            return
        if temp_sum > target:
            return
        for j in range(i, len(candidates)):
            backtrack(j, temp_sum + candidates[j], temp_list + [candidates[j]])

    backtrack(0, 0, [])
    return res