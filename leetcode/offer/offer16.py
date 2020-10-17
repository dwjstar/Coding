def myPow(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    if n%2==0:
        return myPow(x,n//2)**2
    else:
        return x*(myPow(x,(n-1)//2)**2)

if __name__=='__main__':
    res=myPow(2,10)
    print(res)