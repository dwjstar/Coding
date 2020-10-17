import math
def cuttingRope(n):
    a=int(math.sqrt(n))
    x=n-a*(a-1)
    mut=1
    for i in range(a-1):
        mut*=a

    mut=mut*x
    return mut

if __name__=='__main__':
    n=20
    print(cuttingRope(n))