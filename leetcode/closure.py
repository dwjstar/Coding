def outer(a):

    def inner(c):
        b=a+c
        print(b)
    return inner

def outer2(a):
    b=10
    return a+b

if __name__=='__main__':
    demo=outer(5)
    # demo1=outer(5)
    demo(5)
    demo(5)

    # print(demo1)