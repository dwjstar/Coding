def LRU(operators, k):
    # write code here
    lru = []
    dic = {}
    res = []
    for ops in operators:
        opt = ops[0]
        if opt == 1:
            if len(lru) >= k:
                key = lru.pop(0)
                dic.pop(key)
            lru.append(ops[1])
            dic[ops[1]] = ops[2]
        else:
            if ops[1] in lru:
                lru.remove(ops[1])
                lru.append(ops[1])
                val = dic[ops[1]]
            else:
                val = -1
            res.append(val)
    return res

if __name__=='__main__':
    l=[[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]]
    k=3
    # result=LRU(l,k)
    # print(result)
    dic={1:2,3:2,2:2}
    dic.pop(1)
    sorted(dic)
    print(dic)
