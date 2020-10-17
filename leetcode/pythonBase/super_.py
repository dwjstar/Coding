import inspect
class A:
    def __init__(self):
        print("A")
    def show(self):
        print('A-show')

class B():
    def __init__(self):
        print('B')
    def show(self):
        print('B-show')

class C(A):
    def __init__(self):
        print('C')

class D(B,A):
    def __init__(self):
        print('D')
    # def show(self):
    #     print('D-show')

if __name__=='__main__':
    d=D()

    d.show()
    print(D.__mro__)
    # print(inspect.getmro(D))