def hanoid(n,a,b,c):
    if n<=0:
        return
    hanoid(n-1,a,c,b)
    move(a,c)
    hanoid(n-1,b,a,c)

def move(a,b):
    print('%s -> %s' %(a ,b))

if __name__=='__main__':
    li=[[1,2,3],[4,5,6],[7,8,9]]
    for i in range(len(li)):
        print(*li[i], sep=' ')