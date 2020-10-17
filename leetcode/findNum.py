def FindNumsAppearOnce( array):
    # write code here
    dic = {}
    res = []
    for i in array:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for k, v in dic.items():
        if v == 1:
            res.append(k)
    return res


if __name__=='__main__':
    arr=[2,4,3,6,3,2,5,5]
    brr=[9,0,8]
    arr.append(brr)
    print(arr)