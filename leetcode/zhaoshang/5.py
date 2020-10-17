def check_(n):
    if n<2:
        return n
    for i in range(2,n):
        if n%i==0:
            return 0
    return n

if __name__=='__main__':
    print(check_(7))