def LFU( operators, k):
    # write code here
    lfu_t = [ [] for i in range(100)]
    dic = {}
    res = []
    for ops in operators:
        opt = ops[0]
        if opt == 1:
            if ops[1] not in dic:
                dic[ops[1]]=[]
                dic[ops[1]].append(ops[2])
                dic[ops[1]].append(1)
                lfu_t[1].append(ops[1])
            else:
                dic[ops[1]][0]=ops[2]
                lfu_t[dic[ops[1]][1]].remove(ops[1])
                dic[ops[1]][1]+=1
                lfu_t[dic[ops[1]][1]].append(ops[1])
            if len(dic) > k:
                for key in lfu_t:
                    if len(key)>0 :
                        key_key=key.pop(0)
                        dic.pop(key_key)
                        break
        elif opt == 2:
            if ops[1] not in dic:
                val = -1
            else:
                val=dic[ops[1]][0]
                lfu_t[dic[ops[1]][1]].remove(ops[1])
                dic[ops[1]][1] += 1
                lfu_t[dic[ops[1]][1]].append(ops[1])
            res.append(val)
    return res

if __name__=='__main__':
    l=[[1,1,1],[1,2,2],[1,3,2],[1,2,4],[1,3,5],[2,2],[1,4,4],[2,1]]
    k=3
    result=LFU(l,k)
    print(result)