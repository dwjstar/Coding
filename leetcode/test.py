import random
def shutff(nums):
    n=len(nums)
    for i in range(n-1):
        x=random.randint(0,n-2-i)
        nums[x],nums[n-1-i]=nums[n-1-i],nums[x]
    return nums

if __name__=='__main__':
    nums=[1,2,3,4,5,6,7,8]
    res=shutff(nums)
    print(res)