def movingCount(m: int, n: int, k: int) -> int:
    if k==0:
        return 1
    visited=set()
    r,d=(1,0),(0,1)
    def is_path(i,j):
        if i<0 or j<0:
            return False
        if i>=m or j>=n:
            return False
        if (i,j) in visited:
            return False
        if ch_(i)+ch_(j)>k:
            return False
        return True
    def ch_(x):
        if x>=10:
            str_x=str(x)
            a,b=int(str_x[0]),int(str_x[1])
            sum_=a+b
        else:
            sum_=x
        return sum_
    q=[]
    q.append((0,0))
    res=1
    while q:
        v=q.pop(0)
        if is_path(v[0]+d[0],v[1]+d[1]):
            q.append((v[0]+d[0],v[1]+d[1]))
            res+=1
            visited.add((v[0]+d[0],v[1]+d[1]))
        if is_path(v[0]+r[0],v[1]+r[1]):
            q.append((v[0] + r[0], v[1] + r[1]))
            res+=1
            visited.add((v[0] + r[0], v[1] + r[1]))
    return res

if __name__=='__main__':
    m=3
    n=2
    k=17
    res=movingCount(m,n,k)
    print(res)
