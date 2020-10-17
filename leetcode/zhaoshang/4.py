import re
string='{(A->B),(B->C),(C->D),(D->A)}'

string_list=string.strip('{}').strip(',').split(',')
dic_={}
def dfs(g,v,visited,res):
    if not g.get(v):
        return
    v_list=g[v]
    for i in v_list:
        if i not in visited:
            visited.append(i)
            dfs(g,i,visited,res)
        else:
            res.append(1)
            return 1
    return 0
for c in string_list:
    if len(c)<6:
        print(-1)
    if c[0]!='(' and c[2]!='-' and c[3]!='>' and c[5]!=')':
        print(-1)
    if c[1].isalpha() and c[4].isalpha():
        if c[1] not in dic_:
            dic_[c[1]]=[]
        dic_[c[1]].append(c[4])
    else:
        print(-1)
res=[]
for k,v in dic_.items():
    visited=[]
    flag=dfs(dic_,k,visited,res)
    print(visited)
    print(flag)
print(res)






print(string_list)
print(dic_)