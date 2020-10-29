def max_sub(nums):
    nums = list(set(nums))
    len_nums = len(nums)
    if len_nums == 1:
        return 1

    nums.sort()
    print(nums)
    flags = [0] * len_nums
    for i in range(1, len_nums):
        flags[i] = nums[i] - nums[i - 1]
    print(flags)
    cnt = 0
    _max = 1
    for i in range(len_nums):
        if flags[i] == 1 and flags[i - 1] == 1:
            cnt += 1
            if cnt > _max:
                _max = cnt
        else:
            cnt = 1
    return _max + 1


if __name__ == '__main__':
    a = [5, 5, 3, 2, 6, 4, 3]
    res = max_sub(a)
    print(res)
